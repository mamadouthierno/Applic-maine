import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils import load_data  # Vérifie que cette fonction existe dans utils.py

# 💅 CSS personnalisé
st.markdown("""
<style>
    .header-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border-left: 5px solid #2e77d0;
    }
    .metric-box {
        background-color: #f2f8ff;
        padding: 1.2rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .metric-value {
        font-size: 2rem;
        color: #2e77d0;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def analyse_descriptive():
    st.title("🔍 Analyse Exploratoire des Données")

    df = load_data()

    if df.empty:
        st.error("❌ Aucune donnée disponible.")
        return

    # ══════════ Aperçu général ══════════
    with st.container():
        st.markdown("<div class='header-card'>", unsafe_allow_html=True)
        st.subheader("📁 Vue d'Ensemble des Données")
        st.dataframe(df.head(), height=250, use_container_width=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"<div class='metric-box'>Patients<br><span class='metric-value'>{df.shape[0]}</span></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='metric-box'>Variables<br><span class='metric-value'>{df.shape[1]}</span></div>", unsafe_allow_html=True)
        with c3:
            missing_total = df.isna().sum().sum()
            missing_pct = df.isna().mean().mean() * 100
            st.markdown(f"<div class='metric-box'>Manquants<br><span class='metric-value'>{missing_total} ({missing_pct:.1f}%)</span></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ══════════ Statistiques descriptives ══════════
    with st.container():
        st.markdown("<div class='header-card'>", unsafe_allow_html=True)
        st.subheader("📊 Statistiques Descriptives")

        selected_var = st.selectbox("🔘 Choisissez une variable :", df.columns)

        if pd.api.types.is_numeric_dtype(df[selected_var]):
            stats = df[selected_var].describe()
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Moyenne", f"{stats['mean']:.2f}")
            col2.metric("Médiane", f"{df[selected_var].median():.2f}")
            col3.metric("Écart-Type", f"{stats['std']:.2f}")
            col4.metric("Valeurs Uniques", df[selected_var].nunique())

            fig = px.histogram(df, x=selected_var, nbins=30, color_discrete_sequence=['#2e77d0'])
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.info(f"🔡 Variable catégorielle sélectionnée : **{selected_var}**")
            cat_counts = df[selected_var].value_counts().reset_index()
            cat_counts.columns = [selected_var, "Effectif"]

            fig = px.bar(cat_counts, x=selected_var, y="Effectif",
                         color="Effectif", color_continuous_scale='Blues')
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(cat_counts)
        st.markdown("</div>", unsafe_allow_html=True)

    # ══════════ Matrice de corrélation ══════════
    with st.container():
        st.markdown("<div class='header-card'>", unsafe_allow_html=True)
        st.subheader("🔗 Matrice de Corrélation")

        numeric_df = df.select_dtypes(include='number')
        if not numeric_df.empty:
            corr_matrix = numeric_df.corr()
            fig = go.Figure(data=go.Heatmap(
                z=corr_matrix.values,
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                colorscale='Blues',
                zmin=-1,
                zmax=1,
                hoverongaps=False
            ))
            fig.update_layout(title="Corrélation des Variables Numériques", height=500)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("⚠️ Aucune variable numérique détectée.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ══════════ Analyse des valeurs manquantes ══════════
    with st.container():
        st.markdown("<div class='header-card'>", unsafe_allow_html=True)
        st.subheader("🔎 Données Manquantes")

        missing = df.isna().sum()
        missing = missing[missing > 0].sort_values(ascending=False).reset_index()
        missing.columns = ["Variable", "Valeurs Manquantes"]

        if not missing.empty:
            fig = px.bar(missing, x="Variable", y="Valeurs Manquantes",
                         color="Valeurs Manquantes", color_continuous_scale="Blues")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(missing)
        else:
            st.success("✅ Aucune valeur manquante détectée.")
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    analyse_descriptive()
