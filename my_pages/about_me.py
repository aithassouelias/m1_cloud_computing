import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

def run():
    # Titre principal
    st.title("🎯 Transformons ensemble vos données en stratégies gagnantes")

    # Bannière ou introduction
    st.write("""
            ---
    Bonjour, moi c'est Elias. Étudiant en **Master Informatique** (Big Data et BI), 
    """)

    # Sous-section 1 : Expériences professionnelles
    st.header("🏆 Mon Palmarès")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👨🏽‍💻 Expériences")
        st.write("""
        - **Consultant Business Intelligence - KPMG**  
        *Stage de 5 mois* - Strasbourg, France 

        - **Data Analyst - CEREMA**  
        *CDD 1 mois* - Metz, France  
                
        - **Data Analyst - CEREMA**  
        *Stage de 3 mois* - Metz, France  
        """)
    with col2 :

        # Sous-section 2 : Diplômes
        st.subheader("🎓 Diplômes")
        st.write("""
        - **Master Informatique**
        *Université de Lyon*, 2024 - à ce jour

        - **Bachelor Science des données**  (Mention Bien)
        *IUT de Metz*, 2021 - 2024
        """)

    # Section 3 : Compétences techniques (outils)
    st.header("🛠️ Mes outils favoris")
    tools = {
        "⚡ Langages": ["Python", "SQL"],
        "📊 Outils": ["Power BI", "Tableau", "Excel"],
        "📚 Bases de données": ["PostgreSQL", "MySQL"],
        "⚙️ Autres": ["Streamlit", "Flask", "..."],
    }
    for category, tool_list in tools.items():
        st.markdown(f"**{category}** : {', '.join(tool_list)}")

    # Section: Skills
    st.header("🌟 Mes compétences clés")

    # Data for hard skills
    hard_skills = {
        "Compétences": ["Traitement de données", "Analyse de données", "Visualisation de données", "Machine Learning", "Business Intelligence"],
        "Niveau de maîtrise (%)": [90, 85, 80, 70, 75]
    }

    # Data for soft skills
    soft_skills = {
        "Compétences": ["Communication", "Travail d'équipe", "Adaptabilité", "Résolution de problèmes", "Gestion du temps"],
        "Niveau de maîtrise (%)": [85, 90, 80, 75, 85]
    }

    # Convert to DataFrame
    df_hard = pd.DataFrame(hard_skills)
    df_soft = pd.DataFrame(soft_skills)

    # Radar chart for hard skills
    fig_hard = px.line_polar(df_hard, r="Niveau de maîtrise (%)", theta="Compétences",
                            line_close=True, 
                            title="Hard Skills",
                            range_r=[0, 100])
    fig_hard.update_traces(fill='toself', line_color="royalblue")
    fig_hard.update_layout(polar=dict(radialaxis=dict(showticklabels=True, ticks='')))

    # Radar chart for soft skills
    fig_soft = px.line_polar(df_soft, r="Niveau de maîtrise (%)", theta="Compétences",
                            line_close=True, 
                            title="Soft Skills",
                            range_r=[0, 100])
    fig_soft.update_traces(fill='toself', line_color="seagreen")
    fig_soft.update_layout(polar=dict(radialaxis=dict(showticklabels=True, ticks='')))

    # Display charts side-by-side in Streamlit

    st.plotly_chart(fig_hard, use_container_width=True)


    st.plotly_chart(fig_soft, use_container_width=True)

    # Section 5 : Prochains objectifs ("Prochain match")
    st.header("🎯 Prochain match")
    st.write("""
    - **Obtenir un stage de 3 mois** à partir d'**avril 2025**, idéalement dans un rôle de Business Intelligence ou Data Science.  
    """)

    # Section : Rejoindre une équipe
    st.header("⚽ Prêt à rejoindre votre équipe !")
    st.markdown("""
    - **[LinkedIn](https://www.linkedin.com/in/aithassouelias/)**
    - **[Curriculum Vitæ](https://drive.google.com/file/d/1d0hXrDvhIWZ27HldwTvDAKvA3WiPlmAk/view?usp=sharing)**
    """)