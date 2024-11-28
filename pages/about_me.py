import streamlit as st

# Titre principal
st.title("À propos de moi")

# Section 1: Présentation générale avec une image d'avatar (optionnel)
st.write("### Présentation")
st.write("""
Bonjour, moi c'est **Elias**, passionné par la **Data Science** et la **Business Intelligence**. 
Je combine une forte expertise technique avec des compétences solides en communication pour offrir des solutions innovantes et basées sur des données. 

### Mes Compétences
Voici un aperçu de mes compétences :

**Data Science & Business Intelligence** :
- Analyse de données
- Visualisation des données
- Modélisation prédictive
- Machine Learning

**Outils et Technologies** :
- Python, R
- SQL, Tableau, Power BI

**Soft Skills** :
- Communication claire avec les clients
- Gestion de projet
- Esprit d'équipe
- Résolution de problèmes

""")

# Section 2: Profil façon FIFA avec des données factices
st.write("### Qui suis-je ?")

# Simuler un profil à la manière d'un joueur FIFA
st.write("**Nom** : Elias")
st.write("**Âge** : 22 ans")
st.write("**Position** : Data Analyst / Consultant Business Intelligence")
st.write("**Note générale** : 86")

# Afficher des statistiques sous forme de barres (à la manière d'un joueur FIFA)
import plotly.graph_objects as go

# Données factices pour les compétences (à ajuster avec tes propres valeurs)
categories = ['Data Science', 'Business Intelligence', 'Soft Skills', 'Résolution de Problèmes', 'Analyse de Données', 'Modélisation Prédictive']
values = [90, 85, 80, 95, 88, 92]  # Remplace par tes propres scores

# Création du radar chart
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values,
    theta=categories,
    fill='toself',
    name='Compétences',
    line_color='blue'
))

fig.update_layout(
    title="Mes Compétences en Data Science & BI",
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    showlegend=False
)

# Afficher le radar chart
st.plotly_chart(fig)

# Section 3: Mon parcours professionnel avec logo KPMG et Cerema
st.write("### Mon Parcours Professionnel 💼")
st.write("""
J'ai eu la chance de travailler avec des entreprises de renom où j'ai acquis une expérience précieuse dans le domaine de la **Data Science** et de la **Business Intelligence**.
Voici un aperçu de mes dernières expériences :

- **KPMG** : Consultant Business Intelligence (2023-2024)
- Création de tableaux de bord financiers et opérationnels
- Collaboration avec des équipes multidisciplinaires pour générer des insights stratégiques
- Utilisation d'outils comme Tableau et Power BI pour l'analyse des données

- **Cerema** : Stagiaire Data Scientist (2022-2023)
- Analyse et prévision des tendances économiques à partir de grandes bases de données
- Développement de modèles statistiques pour l'optimisation des processus décisionnels

""")

# Ajouter les logos des entreprises
col1, col2 = st.columns(2)
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/KPMG_logo.svg/1280px-KPMG_logo.svg.png", width=200)
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Cerema_logo_2021.svg", width=200)

# Section 4: Liens vers le CV et LinkedIn
st.write("### Liens Utiles 🔗")
st.write("""
- **Mon CV** : [Télécharger mon CV](https://tonlienverstoncv.com)
- **LinkedIn** : [Mon profil LinkedIn](https://www.linkedin.com/in/tonnom)
""")

# Section 5: Message de clôture
st.write("### En résumé")
st.write("""
Je suis un professionnel enthousiaste de la **Data Science** et de la **Business Intelligence**, toujours à la recherche de nouveaux défis. Si vous cherchez un expert pour analyser vos données et fournir des solutions stratégiques basées sur ces informations, n'hésitez pas à me contacter !

Merci de visiter mon profil et de découvrir mes compétences et mon parcours.
""")