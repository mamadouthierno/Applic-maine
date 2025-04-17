from PIL import Image
import streamlit as st
import os
from utils import LOGO_PATH
import base64

# Fonction pour convertir une image en base64
def get_base64_bg(path):
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

def accueil():
    bg_image = get_base64_bg("assets/background.jpeg")  # Image de fond

    st.markdown(f"""
        <style>
            :root {{
                --primary-color: #2E8B57;
                --secondary-color: #3CB371;
                --dark-green: #006400;
                --light-bg: #F0F4F8;
            }}
            
            .custom-bg {{
                background-image: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)), url("{bg_image}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 80vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
                margin-bottom: 3rem;
            }}

            .main-title {{
                font-size: 4rem;
                font-weight: 700;
                color: var(--dark-green);
                margin-bottom: 2rem;
                text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
                animation: fadeInTitle 1.5s ease-in-out;
            }}

            .sub-title {{
                font-size: 2rem;
                font-weight: 600;
                color: var(--dark-green);
                margin-bottom: 1.5rem;
                animation: fadeInSubTitle 2s ease-in-out;
            }}

            .custom-btn {{
                padding: 12px 30px;
                font-size: 1.2rem;
                color: white;
                background: linear-gradient(to right, var(--primary-color), var(--dark-green));
                border: none;
                border-radius: 8px;
                margin-top: 1rem;
                cursor: pointer;
                transition: all 0.3s ease;
                animation: fadeInButton 2.5s ease-in-out;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .custom-btn:hover {{
                transform: translateY(-2px);
                box-shadow: 0 6px 8px rgba(0,0,0,0.15);
                background: linear-gradient(to right, var(--secondary-color), var(--primary-color));
            }}

            @keyframes fadeInTitle {{
                0% {{ opacity: 0; transform: translateY(-30px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}
            
            @keyframes fadeInSubTitle {{
                0% {{ opacity: 0; transform: translateY(30px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}
            
            @keyframes fadeInButton {{
                0% {{ opacity: 0; transform: scale(0.9); }}
                100% {{ opacity: 1; transform: scale(1); }}
            }}

            .content-section {{
                background-color: var(--light-bg);
                padding: 3rem 2rem;
                text-align: center;
                border-radius: 10px;
                margin: 2rem 0;
                animation: slideInUp 1.5s ease-in-out;
            }}
            
            .content-section h2 {{
                font-size: 2.5rem;
                color: var(--dark-green);
                margin-bottom: 1.5rem;
            }}
            
            .benefits {{
                list-style-type: none;
                padding: 0;
                max-width: 800px;
                margin: 0 auto 2rem auto;
            }}
            
            .benefits li {{
                font-size: 1.2rem;
                padding: 0.8rem;
                margin: 0.5rem 0;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            
            .benefits li:before {{
                content: "✓";
                color: var(--primary-color);
                font-weight: bold;
                margin-right: 10px;
                font-size: 1.3rem;
            }}
            
            .call-to-action {{
                margin-top: 2rem;
                font-size: 1.3rem;
                font-weight: 500;
                color: var(--dark-green);
            }}
            
            @keyframes slideInUp {{
                0% {{ opacity: 0; transform: translateY(30px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}
            
            @media (max-width: 768px) {{
                .main-title {{
                    font-size: 2.5rem;
                }}
                .sub-title {{
                    font-size: 1.5rem;
                }}
                .custom-bg {{
                    height: 60vh;
                    padding: 1rem;
                }}
            }}
        </style>

        <!-- Hero Section -->
        <div class="custom-bg">
            <h1 class="main-title">L'Ère Nouvelle de la Médecine Intelligente</h1>
            <h2 class="sub-title">Plateforme IA de pointe pour la lutte contre les cancers digestifs</h2>
            <button class="custom-btn" onclick="window.scrollTo({{top: document.querySelector('.content-section').offsetTop, behavior: 'smooth'}})">Découvrir la Technologie</button>
        </div>

        <!-- Content Section -->
        <div class="content-section">
            <h2>Révolution dans la prise en charge des cancers digestifs</h2>
            <p>Notre plateforme IA transforme l'oncologie digestive avec :</p>
            
            <ul class="benefits">
                <li>Modèles prédictifs de survie certifiés avec une précision de 95%</li>
                <li>Protocoles thérapeutiques optimisés par intelligence artificielle</li>
                <li>Profilage moléculaire personnalisé pour chaque patient</li>
                <li>Analyse en temps réel des données cliniques</li>
            </ul>

            <div class="call-to-action">
                <p>Rejoignez la médecine oncologique de demain dès aujourd'hui</p>
                <button class="custom-btn" style="margin-top: 1rem;">Demander une démonstration</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    accueil()
