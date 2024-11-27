import streamlit as st
import pandas as pd
import plotly.express as px

# Load the datasets
df_players = pd.read_csv("./data/male_players.csv")  # Your football players dataset
df_flags = pd.read_csv("./data/flags_iso.csv")  # Your country flags dataset

# Define the pages as functions
def home_page():

    # Image d'en-tête (optionnel, tu peux ajouter une image si tu veux)
    # st.image("path_to_header_image.jpg", use_column_width=True)

    # Titre principal
    st.title("Bienvenue sur l'outil d'analyse des talents footballistiques ! ⚽")

    # Description rapide
    st.write("Dans cette application, vous allez pouvoir analyser les statistiques de différents joueurs, championnats, équipes et nations pour dénicher les meilleurs talents. Voici quelques points de vue intéressants pour exploiter cet outil :")

    # Séparation avec une ligne
    st.markdown("---")

    # Section 1: Le sélectionneur de nation
    st.subheader("1. Le Sélectionneur de Nation à la recherche de talents 🌍")
    st.image("./assets/wc.jpg")
    st.write("""
        🎯 **Objectif**
             
        - Trouver un joueur spécifique pour compléter une équipe nationale. ⚽

        🔎 **Comment ?**
        - Grâce à des filtres simples, vous pouvez sélectionner un pays et un poste précis. L'application vous fournira une liste de joueurs correspondant à ces critères, avec des statistiques détaillées comme la moyenne d'âge, la note OVR, et bien plus.

        💡 **Exemple pratique**
        - Le sélectionneur d’une équipe nationale peut rechercher des talents pour combler des postes clés dans l’équipe pour une compétition majeure comme la Coupe du Monde. 🏆
    """)


    # Séparation avec une ligne
    st.markdown("---")

    # Section 2: Le recruteur de club
    st.subheader("2. Le Recruteur de Club pour le Mercato 💼")
    st.image("./assets/Messi.jpg")
    st.write("""
        🎯 **Objectif**  
        - Identifier un joueur avec des caractéristiques spécifiques pour le mercato. 

        🔍 **Comment ?**  
        - En sélectionnant des critères comme le poste, l’âge, ou le niveau de performance, l'application crée une vue d’ensemble des joueurs correspondant à ces besoins. 
        Cela permet de trouver un talent prometteur parmi une grande variété de profils.

        💡 **Exemple**  
        - Un club à la recherche d’un attaquant de 23 ans avec un excellent potentiel offensif pourrait facilement obtenir une liste de joueurs qui répondent à ces critères. 
        Ces méthodes sont déjà utilisées par des clubs pour repérer des talents à faible coût mais avec un fort potentiel.
    """)


    # Séparation avec une ligne
    st.markdown("---")

    # Section 3: Le joueur en comparaison
    st.subheader("3. Le Joueur en Comparaison 🆚")
    st.write("""
        🎯 **Objectif**
        - Comparer les statistiques d’un joueur avec celles des autres joueurs du même poste.

        🔍 **Comment ?**
        - En sélectionnant un joueur, vous pouvez accéder à des comparaisons détaillées avec d’autres joueurs du même poste, et analyser des KPIs comme la performance globale (OVR), l’âge moyen des joueurs, leur expérience en compétition, etc.

        💡 **Exemple pratique**
        - Un joueur peut évaluer ses performances en les comparant avec d’autres joueurs du même poste, afin de savoir où il se situe et identifier les domaines à améliorer. 📊
    """)

    # Séparation avec une ligne
    st.markdown("---")

    # Conclusion
    st.write("### En résumé :")
    st.write("""
    Cette application est un véritable **outil d'aide à la décision** pour les recruteurs, sélectionneurs et joueurs. Vous pouvez :
    - **Trouver un futur champion pour la Coupe du Monde**,
    - **Identifier des joueurs pour le mercato**,
    - **Évaluer vos performances par rapport à d'autres joueurs.**

    **Prêt à découvrir la prochaine star du football ?**
    """)

    # Ajouter un petit texte de footer
    st.markdown("---")
    st.write("⚡️ Développé avec Streamlit | Par Elias Ait Hassou")
    
def player_page():
    # Sidebar filter: Select Nation
    Nation = st.sidebar.selectbox('Choisir un pays', df_players['Nation'].unique())
    position = st.sidebar.selectbox('Choisir un poste', df_players['Position'].unique())

    # Find the flag URL for the selected nation
    selected_flag = df_flags[df_flags['Country'] == Nation]

    # If flag URL exists for the selected nation
    if not selected_flag.empty:
        st.write(f" {Nation}")
        flag_url = selected_flag['URL'].iloc[0]  # Flag URL from the CSV
        st.image(flag_url)
    else:
        st.write(f"No flag found for {Nation}")

    # Optionally, display some player data for the selected nation
    players_from_nation = df_players[(df_players['Nation'] == Nation) & (df_players['Position'] == position)]

    # Calculate average age and average OVR
    num_players = len(players_from_nation)
    average_age = players_from_nation['Age'].mean()
    average_OVR = players_from_nation['OVR'].mean()

    # Display the KPI cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Players", f"{num_players:.0f}")

    with col2:
        st.metric("Average Age", f"{average_age:.0f}")

    with col3:
        st.metric("Average OVR", f"{average_OVR:.0f}")

    # Create a bar chart for the top 5 leagues
    league_counts = players_from_nation['League'].value_counts().reset_index()
    league_counts.columns = ['League', 'Number of Players']

    threshold = 5  # For example, leagues with fewer than 5 players will be grouped as "Other"

    # Group small leagues into "Other"
    other_leagues = league_counts[league_counts['Number of Players'] < threshold]
    other_sum = other_leagues['Number of Players'].sum()

    # Create a new row for "Other"
    other_row = pd.DataFrame({'League': ['Other'], 'Number of Players': [other_sum]})

    # Remove small leagues and append the "Other" category
    league_counts = league_counts[league_counts['Number of Players'] >= threshold]
    league_counts = pd.concat([league_counts, other_row], ignore_index=True)

    # Sort again after adding "Other"
    league_counts = league_counts.sort_values(by='Number of Players', ascending=False)

    # Create a donut chart (pie chart with hole)
    fig = px.pie(league_counts, 
                 names='League', 
                 values='Number of Players', 
                 title=f"TOP 5 des championnats dans lesquels évoluent ces joueurs",
                 labels={'League': 'Championnat', 'Number of Players': 'Nombre de joueurs'},
                 hole=0.4)  # Adjust hole parameter to create a donut chart

    # Display the donut chart
    st.plotly_chart(fig)

def statistics_page():
    st.title("Player Statistics")
    st.write("Here you can display various statistics of players like average age, OVR, etc.")

def profile_page():
    # Titre principal
    st.title("À propos de moi")

    # Section 1: Présentation générale avec une image d'avatar (optionnel)
    st.write("### Présentation")
    st.write("""
    Bonjour, je suis **[Ton Nom]**, passionné par la **Data Science** et la **Business Intelligence**. 
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
    - Hadoop, Spark

    **Soft Skills** :
    - Communication claire avec les clients
    - Gestion de projet
    - Esprit d'équipe
    - Résolution de problèmes

    """)

    # Section 2: Profil façon FIFA avec des données factices
    st.write("### Profil de Data Scientist 🚀")

    # Simuler un profil à la manière d'un joueur FIFA
    st.write("**Nom** : [Ton Nom]")
    st.write("**Âge** : 25 ans")
    st.write("**Position** : Data Scientist & Business Intelligence Analyst")
    st.write("**Niveau d'OVR** : 85 (excellente maîtrise des outils BI et techniques de data science)")

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

# Create the main navigation bar in the sidebar
page = st.sidebar.selectbox("Select a Page", ("Page d'accueil", "Portail séléctionneur", "Portail Mercato", "Portail benchmark","A propos de moi"))

# Display the appropriate page based on the selection
if page == "Page d'accueil":
    home_page()
elif page == "Portail séléctionneur":
    player_page()
elif page == "Portail Mercato":
    statistics_page()
elif page == "A propos de moi":
    profile_page()
