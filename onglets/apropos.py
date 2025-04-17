st.markdown(f"""
    <style>
        body {{
            background-color: #f1f5f9;
            font-family: 'Segoe UI', sans-serif;
        }}

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
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            position: relative;
        }}

        .custom-bg::before {{
            content: "";
            position: absolute;
            top: 0; left: 0;
            width: 100%;
            height: 100%;
            background: rgba(15, 23, 42, 0.6); /* Overlay foncé bleu nuit */
            backdrop-filter: blur(4px);
            border-radius: 12px;
        }}

        .custom-bg > * {{
            position: relative;
            z-index: 1;
        }}

        .main-title {{
            font-size: 3.2rem;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 0.5rem;
            text-shadow: 1px 1px 4px #000;
        }}

        .sub-title {{
            font-size: 1.4rem;
            color: #e2e8f0;
            text-shadow: 1px 1px 2px #000;
        }}

        .card {{
            background: rgba(255,255,255,0.95);
            padding: 1rem;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 1rem;
            transition: transform 0.2s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}

        .card:hover {{
            transform: translateY(-4px);
        }}

        .stats-icon {{
            font-size: 2.8rem;
            margin-bottom: 0.3rem;
        }}

        .stat-value {{
            font-size: 2.2rem;
            font-weight: bold;
            color: #0f172a;
        }}

        .stat-label {{
            font-size: 1rem;
            color: #64748b;
        }}

        .team-card {{
            background: #ffffffee;
            border-radius: 12px;
            padding: 1rem;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }}

        .team-card:hover {{
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
            transform: translateY(-5px);
        }}

        .team-card img {{
            border-radius: 10px;
            height: 220px;
            object-fit: cover;
            border: 3px solid #2e77d0;
            margin-bottom: 0.5rem;
        }}

        .team-card h3 {{
            color: #0f172a;
            margin: 0.5rem 0 0.2rem;
        }}

        .team-card p {{
            color: #475569;
        }}
    </style>

    <div class="custom-bg">
        <h1 class="main-title">🩺 Prévision du Temps de Survie du Cancer Gastrique</h1>
        <p class="sub-title">L'intelligence artificielle au service de l'oncologie clinique au Sénégal.</p>
    </div>
""", unsafe_allow_html=True)
