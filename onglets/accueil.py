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
            .custom-bg {{
                background-image: url("{bg_image}");
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
            }}

            /* TITRE PRINCIPAL EN VERT */
st.markdown(f"""
    <style>
        /* TITRE PRINCIPAL */
        .main-title {{
            font-size: 24rem;
            font-weight: bold;
            color: green;
            margin-bottom: 6rem;
            animation: fadeInTitle 3s ease-in-out;
        }}

        /* NOUVEAU : DEUXIÈME TITRE */
        .second-title {{
            font-size: 6rem;
            color: green;
            margin-bottom: 2rem;
            animation: fadeInSubTitle 4s ease-in-out;
        }}

            .custom-btn {{
                padding: 10px 25px;
                font-size: 1.2rem;
                color: white;
                background: linear-gradient(green, #006400);
                border: none;
                border-radius: 8px;
                margin-top: 1rem;
                cursor: pointer;
                transition: all 0.3s ease;
                animation: fadeInButton 5s ease-in-out;
            }}
            .custom-btn:hover {{
                background: linear-gradient(45deg, #76f2b0, #6e7dff);
            }}

            @keyframes fadeInTitle {{
                0% {{ opacity: 0; transform: translateY(-50px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}
            @keyframes fadeInSubTitle {{
                0% {{ opacity: 0; transform: translateY(50px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}
            @keyframes fadeInButton {{
                0% {{ opacity: 0; transform: scale(0.8); }}
                100% {{ opacity: 1; transform: scale(1); }}
            }}

            .impression-section {{
                background-color: #F0F4F8;
                padding: 3rem 0;
                text-align: center;
                animation: slideInUp 2s ease-in-out;
            }}
            .impression-section h2 {{
                font-size: 2.5rem;
                color: green;
                margin-bottom: 2rem;
            }}
            .impression-section p {{
                font-size: 1.2rem;
                color: #334155;
                margin-bottom: 2rem;
            }}
            .highlight-btn {{
                padding: 12px 30px;
                font-size: 1.3rem;
                color: white;
                background: #2e77d0;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: all 0.3s ease;
            }}
            .highlight-btn:hover {{
                background: #1a5fa4;
            }}
            @keyframes slideInUp {{
                0% {{ opacity: 0; transform: translateY(50px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}
        </style>

        <!-- CONTENU HTML -->
        <div class="custom-bg">
            <h1 class="main-title">L'Innovation Médicale Redéfinie</h1>
            <h2 class="sub-title">Plateforme IA de pointe pour la lutte contre les cancers digestifs</h2>
            <button class="custom-btn">Découvrir la Technologie</button>
        </div>

        <!-- SECTION IMPRESSIONNANTE -->
        <div class="impression-section">
            <h2>Un Futur Prometteur avec l'IA</h2>
            <p>Notre plateforme révolutionne l'approche diagnostique et thérapeutique des cancers digestifs, en vous offrant des prédictions de survie précises et des solutions innovantes basées sur l'intelligence artificielle.</p>
            <button class="highlight-btn">Explorez Notre Solution</button>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    accueil()
