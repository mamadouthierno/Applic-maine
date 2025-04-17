import streamlit as st  
import numpy as np  
import plotly.express as px  
from datetime import date  
import io  
from fpdf import FPDF  
from utils import (
    FEATURE_CONFIG,
    encode_features,
    load_model,
    predict_survival,
    clean_prediction,
    save_new_patient,
    MODELS
)

# 🎨 CSS personnalisé avec bannière verte et fond vert clair  
st.markdown("""  
<style>  
    body, .stApp {  
        background-color: #e6f4ea !important;  /* 💚 fond général vert très clair */  
    }  
    .st-emotion-cache-1y4p8pa {  
        padding: 2rem 1rem;  
    }  
    .form-card, .header-card, .prediction-card {  
        background: white;  
        border-radius: 15px;  
        padding: 2rem;  
        margin-bottom: 2rem;  
        box-shadow: 0 4px 20px rgba(0,0,0,0.06);  
    }  
    .form-title {  
        font-size: 1.6rem;  
        font-weight: bold;  
        color: #2e7d32;  /* 💚 vert foncé pour le titre formulaire */  
        margin-bottom: 1rem;  
    }  
    h1 {  
        color: #2e7d32 !important;  /* 💚 titre principal en vert foncé */  
        background-color: #c8e6c9 !important;  /* 💚 bannière verte claire */  
        padding: 1rem;  
        border-radius: 10px;  
        text-align: center;  
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);  
    }  
    .stButton>button {  
        background: linear-gradient(45deg, #2e7d32, #66bb6a) !important;  
        color: white !important;  
        border-radius: 10px !important;  
        padding: 0.75rem 2rem !important;  
        border: none !important;  
        transition: all 0.3s ease-in-out;  
    }  
    .stButton>button:hover {  
        transform: translateY(-2px);  
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.4);  
    }  
</style>  
""", unsafe_allow_html=True)

# Le reste du code reste identique à ce que tu avais  
def generate_pdf_report(input_data, cleaned_pred):  
    pdf = FPDF()  
    pdf.add_page()  
    pdf.set_font('Arial', 'B', 24)  
    pdf.set_text_color(46, 119, 208)  
    pdf.cell(0, 15, "Rapport Médical MED-AI", ln=True, align='C')  
  
    pdf.set_font('Arial', '', 12)  
    pdf.set_text_color(0, 0, 0)  
    pdf.cell(0, 10, f"Date : {date.today().strftime('%d/%m/%Y')}", ln=True)  
  
    pdf.set_font('Arial', 'B', 16)  
    pdf.cell(0, 15, "Paramètres Cliniques", ln=True)  
    pdf.set_fill_color(240, 248, 255)  
  
    pdf.set_font('Arial', '', 12)  
    col_widths = [60, 60]  
    for key, value in input_data.items():  
        pdf.cell(col_widths[0], 8, FEATURE_CONFIG.get(key, key), 1, 0, 'L', 1)  
        pdf.cell(col_widths[1], 8, str(value), 1, 1, 'L')  
  
    pdf.set_font('Arial', 'B', 16)  
    pdf.cell(0, 15, "Résultats de Prédiction", ln=True)  
    pdf.set_font('Arial', '', 14)  
    pdf.cell(0, 8, "Modèle utilisé : DeepSurv", ln=True)  
    pdf.set_text_color(46, 119, 208)  
    pdf.cell(0, 8, f"Survie médiane estimée : {cleaned_pred:.1f} mois", ln=True)  
  
    pdf_buffer = io.BytesIO()  
    pdf.output(pdf_buffer)  
    return pdf_buffer.getvalue()  

def modelisation():  
    st.title("🧬 Analyse de Survie Médicale")  
  
    with st.container():  
        st.markdown("<div class='form-card'>", unsafe_allow_html=True)  
        st.markdown("<div class='form-title'>📋 Informations Patient</div>", unsafe_allow_html=True)  
        inputs = {}  
        cols = st.columns(3)  
        for i, (feature, label) in enumerate(FEATURE_CONFIG.items()):  
            with cols[i % 3]:  
                if feature == "AGE":  
                    inputs[feature] = st.number_input(label, min_value=18, max_value=120, value=50)  
                else:  
                    inputs[feature] = st.selectbox(label, options=["Non", "Oui"])  
        st.markdown("</div>", unsafe_allow_html=True)  
  
    input_df = encode_features(inputs)  
    model_name = "DeepSurv"  
  
    if st.button("🔮 Calculer la Prédiction", use_container_width=True):  
        with st.spinner("Analyse en cours..."):  
            try:  
                model = load_model(MODELS[model_name])  
                pred = predict_survival(model, input_df)  
                cleaned_pred = clean_prediction(pred)  
  
                patient_data = input_df.to_dict(orient='records')[0]  
                patient_data["Tempsdesuivi"] = round(cleaned_pred, 1)  
                patient_data["Deces"] = "OUI"  
  
                save_new_patient(patient_data)  
  
                st.markdown("<div class='prediction-card'>", unsafe_allow_html=True)  
                col1, col2 = st.columns([1, 2])  
                with col1:  
                    st.metric("Survie Médiane Estimée", f"{cleaned_pred:.0f} mois")  
                with col2:  
                    months = min(int(cleaned_pred), 120)  
                    survival_curve = [100 * np.exp(-np.log(2) * t / cleaned_pred) for t in range(months)]  
                    fig = px.line(  
                        x=list(range(months)),  
                        y=survival_curve,  
                        labels={"x": "Mois", "y": "Probabilité de Survie (%)"},  
                        color_discrete_sequence=['#2e7d32']  
                    )  
                    st.plotly_chart(fig, use_container_width=True)  
                st.markdown("</div>", unsafe_allow_html=True)  
  
                pdf_bytes = generate_pdf_report(patient_data, cleaned_pred)  
                st.download_button("📥 Télécharger le Rapport", data=pdf_bytes, file_name="rapport_medical.pdf", mime="application/pdf", use_container_width=True)  
            except Exception as e:  
                st.error(f"Erreur : {str(e)}")  
  
    st.markdown("---")  
    with st.expander("📅 Planification du Suivi"):  
        col1, col2 = st.columns(2)  
        with col1:  
            selected_treatments = st.multiselect("Traitements Recommandés", ["Chimiothérapie", "Exclusive"])  
        with col2:  
            follow_up_date = st.date_input("Date Suivi Recommandée", value=date.today())  
  
        if st.button("💾 Enregistrer le Plan", use_container_width=True):  
            if selected_treatments:  
                st.toast("Plan de traitement sauvegardé ✅")  
            else:  
                st.warning("Veuillez sélectionner au moins un traitement")  
  
if __name__ == "__main__":  
    modelisation()
