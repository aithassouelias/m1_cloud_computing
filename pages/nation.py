import streamlit as st
import pandas as pd
import plotly.express as px
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
def draw_pitch():
        # Dimensions du terrain (en mètres)
        fig, ax = plt.subplots(figsize=(10, 7))
        
        # Ligne de touche
        plt.plot([0, 105, 105, 0, 0], [0, 0, 68, 68, 0], color="black", linewidth=2)
        # Lignes du milieu
        plt.plot([52.5, 52.5], [0, 68], color="black", linewidth=2)
        # Surface de réparation
        plt.plot([16.5, 16.5], [13.84, 68-13.84], color="black", linewidth=2)
        plt.plot([105-16.5, 105-16.5], [13.84, 68-13.84], color="black", linewidth=2)
        plt.plot([0, 16.5], [13.84, 13.84], color="black", linewidth=2)
        plt.plot([0, 16.5], [68-13.84, 68-13.84], color="black", linewidth=2)
        plt.plot([105, 105-16.5], [13.84, 13.84], color="black", linewidth=2)
        plt.plot([105, 105-16.5], [68-13.84, 68-13.84], color="black", linewidth=2)
        # Cercle central
        centre_circle = plt.Circle((52.5, 34), 9.15, color="black", fill=False, linewidth=2)
        ax.add_patch(centre_circle)
        plt.scatter(52.5, 34, color="black", s=10)  # Point central
        
        return fig, ax


def nation_page(df_players, df_flags):
    # Sidebar filter: Select Nation
    st.title("Portail sélectionneur")
    col1, col2 = st.columns(2)
    with col1: 
        Nation = st.selectbox('Choisir un pays', df_players['Nation'].unique())
    with col2: 
        ovr_range = st.slider(
            "Select OVR Range", 
            min_value=int(df_players['OVR'].min()),  # Minimum OVR value
            max_value=int(df_players['OVR'].max()),  # Maximum OVR value
            value=(int(df_players['OVR'].min()), int(df_players['OVR'].max())),  # Default range (min to max)
            step=1  # Step for slider (e.g., 1)
        )

    # Find the flag URL for the selected nation
    selected_flag = df_flags[(df_flags['Country'] == Nation)]

    # Optionally, display some player data for the selected nation
    players_from_nation = df_players[(df_players['Nation'] == Nation) & (df_players['OVR'] >= ovr_range[0]) & (df_players['OVR'] <= ovr_range[1])]

    # Calculate average age and average OVR
    num_players = len(players_from_nation)
    average_age = players_from_nation['Age'].mean()
    average_OVR = players_from_nation['OVR'].mean()

    # Display the KPI cards
    col0, col1, col2, col3 = st.columns(4)

    with col0:
        flag_url = selected_flag['URL'].iloc[0]  # Flag URL from the CSV
        st.image(flag_url)
    with col1:
        st.metric("Nombre de joueurs", f"{num_players:.0f}")

    with col2:
        st.metric("Age moyen", f"{average_age:.0f}")

    with col3:
        st.metric("Note générale moyenne", f"{average_OVR:.0f}")

    fig, ax = draw_pitch()
    # Mapping des positions à des coordonnées sur le terrain
    position_coords = {
        "GK": (5, 34),   # Gardien
        "CB": (25, 34),  # Défenseur central
        "LB": (25, 10),  # Défenseur gauche
        "RB": (25, 58),  # Défenseur droit
        "CM": (50, 34),  # Milieu central
        "LW": (75, 10),  # Ailier gauche
        "RW": (75, 58),  # Ailier droit
        "ST": (95, 34),  # Attaquant
    }

    # Ajouter un filtre sur la Nation
    filtered_df = players_from_nation

    # Compter le nombre de joueurs par position
    position_counts = filtered_df['Position'].value_counts()
    

    # Normalize la couleur des cercles en fonction du nombre de joueurs
    norm = plt.Normalize(vmin=position_counts.min(), vmax=position_counts.max())
    cmap = plt.cm.get_cmap("YlOrRd")  # Choisir une palette de couleur

    # Ajouter des cercles et le nombre de joueurs pour chaque position
    for position, coord in position_coords.items():
        count = position_counts.get(position, 0)  # Récupérer le compte ou 0
        if count > 0:
            # Ajuster la taille du cercle en fonction du nombre de joueurs
        
            # Choisir la couleur en fonction du nombre de joueurs
            color = cmap(norm(count))
            
            # Dessiner un cercle
            circle = Circle(coord, color=color, ec="white", lw=1, alpha=0.8)
            ax.add_patch(circle)
            # Ajouter le nombre de joueurs
            ax.text(
                coord[0], coord[1],
                str(count),
                color="black", fontsize=10, ha="center", va="center", fontweight="bold"
            )
    ax.axis("off")  
    # Afficher le terrain sur Streamlit
    st.pyplot(fig)
    
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

    
