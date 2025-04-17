import streamlit as st
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "votre-email@gmail.com"
EMAIL_PASSWORD = "12_SEFD"
EMAIL_RECEIVER = "mamadouthierno@gmail.com"

def send_email(name, sender_email, message):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = f"📬 Nouveau contact MEDCINE-AI : {name}"
        
        html = f"""
        <html>
          <body style="margin: 0; font-family: 'Segoe UI', sans-serif;">
            <div style="background: #f8faff; padding: 40px;">
              <div style="max-width: 600px; margin: 0 auto; background: white; border-radius: 16px; box-shadow: 0 4px 24px rgba(0,0,0,0.08);">
                <div style="padding: 40px; text-align: center;">
                  <img src="https://i.ibb.co.com/logo.png" alt="MED-AI Logo" style="height: 60px; margin-bottom: 30px;">
                  <div style="background: linear-gradient(135deg, #2e77d0, #22d3ee); padding: 20px; border-radius: 12px;">
                    <h2 style="color: white; margin: 0;">Nouveau message de {name}</h2>
                  </div>
                  <div style="padding: 30px 20px; text-align: left;">
                    <div style="margin-bottom: 25px;">
                      <p style="font-size: 16px; color: #444; margin: 8px 0;">
                        <strong style="color: #2e77d0;">📧 Email :</strong><br>
                        {sender_email}
                      </p>
                      <p style="font-size: 16px; color: #444; margin: 8px 0;">
                        <strong style="color: #2e77d0;">📝 Message :</strong><br>
                        <div style="background: #f8faff; padding: 15px; border-radius: 8px; margin-top: 10px;">
                          {message}
                        </div>
                      </p>
                    </div>
                    <hr style="border: 1px solid #eee; margin: 30px 0;">
                    <p style="font-size: 14px; color: #888; text-align: center;">
                      Ce message a été envoyé via le formulaire de contact MED-AI
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </body>
        </html>
        """
        
        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        
        return True
    except Exception as e:
        st.error(f"❌ Erreur d'envoi : {str(e)}")
        return False

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

# Interface utilisateur
def main():
    st.set_page_config(page_title="Contact MED-AI", layout="wide")

    st.markdown("""
    <style>
        :root {
            --primary: #2e77d0;
            --secondary: #1d5ba6;
            --accent: #22d3ee;
        }
        .main-container { max-width: 1000px; margin: 2rem auto; padding: 0 1rem; font-family: 'Segoe UI', sans-serif; }
        .contact-header { text-align: center; margin-bottom: 3rem; padding: 2rem; background: linear-gradient(135deg, var(--primary), var(--accent)); border-radius: 16px; color: #fff; }
        .form-card { background: #f8faff; padding: 2.5rem; border-radius: 16px; box-shadow: 0 8px 32px rgba(0,0,0,0.05); margin-bottom: 2rem; }
        .input-field { margin-bottom: 1.8rem; }
        .input-field label { display: block; margin-bottom: 0.6rem; color: var(--primary); font-weight: 500; font-size: 1.1rem; }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            border: 2px solid #e9f2fb !important;
            border-radius: 10px !important;
            padding: 1rem !important;
            font-size: 1rem !important;
            transition: all 0.3s !important;
        }
        .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
            border-color: var(--accent) !important;
            box-shadow: 0 0 0 3px rgba(34, 211, 238, 0.1) !important;
        }
        .submit-btn {
            background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
            color: white !important;
            padding: 1rem 2.5rem !important;
            border-radius: 10px !important;
            font-size: 1.1rem !important;
        }
        .submit-btn:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 15px rgba(46, 119, 208, 0.3) !important;
        }
        .contact-info-card {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.05);
        }
        .info-item {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
            padding: 1.2rem;
            background: #f8faff;
            border-radius: 12px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='main-container'>", unsafe_allow_html=True)

    st.markdown("""
        <div class='contact-header'>
            <h1 style="font-size: 2.5rem; margin-bottom: 1rem;">📬 Contactez Notre Équipe Médicale</h1>
            <p style="font-size: 1.2rem; opacity: 0.9;">Une question ? Un projet ? Nous répondons sous 24h</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        with st.form("contact_form"):
            st.markdown("<div class='form-card'>", unsafe_allow_html=True)

            st.markdown("<div class='input-field'>", unsafe_allow_html=True)
            name = st.text_input("Nom Complet *", placeholder="Dr. Mamadou BOUSSO")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='input-field'>", unsafe_allow_html=True)
            email = st.text_input("Email Professionnel *", placeholder="contact@clinique.com")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='input-field'>", unsafe_allow_html=True)
            message = st.text_area("Message *", height=200, placeholder="Décrivez votre demande en détail…")
            st.markdown("</div>", unsafe_allow_html=True)

            submitted = st.form_submit_button("Envoyer le Message ✉️", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

            if submitted:
                if not name or not email or not message:
                    st.warning("Veuillez remplir tous les champs requis.")
                elif not validate_email(email):
                    st.warning("Adresse email invalide.")
                else:
                    if send_email(name, email, message):
                        st.success("✅ Message envoyé avec succès !")
                    else:
                        st.error("❌ Une erreur est survenue lors de l'envoi.")

    with col2:
        st.markdown("<div class='contact-info-card'>", unsafe_allow_html=True)
        st.markdown("""
            <h3 style="color: var(--primary); margin-bottom: 1.5rem;">📌 Coordonnées</h3>
            <div class='info-item'>
                <div style="margin-right: 1rem;">🏥</div>
                <div>
                    <h4 style="margin: 0; color: var(--secondary);">Clinique MED-AI</h4>
                    <p style="margin: 0.3rem 0 0; color: #666;">123 Rue de la Santé<br>Dakar, Sénégal</p>
                </div>
            </div>
            <div class='info-item'>
                <div style="margin-right: 1rem;">📞</div>
                <div>
                    <h4 style="margin: 0; color: var(--secondary);">Téléphone</h4>
                    <p style="margin: 0.3rem 0 0; color: #666;">+221 77 135 48 03<br>Urgences 24/7</p>
                </div>
            </div>
            <div class='info-item'>
                <div style="margin-right: 1rem;">🌐</div>
                <div>
                    <h4 style="margin: 0; color: var(--secondary);">Réseaux Sociaux</h4>
                    <div style="display: flex; gap: 1rem; margin-top: 0.5rem;">
                        <a href="https://www.linkedin.com/in/mamadouthierno" target="_blank" style="color: var(--primary); text-decoration: none;">🔗 LinkedIn</a>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
