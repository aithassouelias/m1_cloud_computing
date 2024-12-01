import streamlit as st

def run():


    # Titre principal
    st.title("TalentTraker, détectez les étoiles montantes du football 🎯")

    # Description rapide
    st.write("Avec Talent Tracker, vous allez pouvoir analyser les statistiques de différents joueurs, championnats, équipes et nations pour dénicher les meilleurs talents. Voici quelques points de vue intéressants pour exploiter cet outil :")

    # Séparation avec une ligne
    st.markdown("---")

    # Section 1: Le sélectionneur de nation
    st.subheader("1. Explorez les talents de chaque nation 🌍")
    st.image("./assets/worldcup.jpeg")
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
    st.subheader("2. Trouvez les meilleurs joueurs pour le Mercato 💼")
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
    st.image("./assets/knn_2.png")
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

    st.markdown("---")
    st.write("⚡️ Développé avec Streamlit | Par Elias Ait Hassou")