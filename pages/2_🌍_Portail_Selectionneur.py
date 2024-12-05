import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.colors as mcolors
from models.db import get_players_by_nation, get_flag_by_nation, get_all_nations

# Fonction pour dessiner un terrain de football
def draw_pitch():
    fig, ax = plt.subplots(figsize=(10, 7))
    # Dessiner les différentes parties du terrain
    plt.plot([0, 105, 105, 0, 0], [0, 0, 68, 68, 0], color="black", linewidth=2)
    plt.plot([52.5, 52.5], [0, 68], color="black", linewidth=2)
    plt.plot([16.5, 16.5], [13.84, 68-13.84], color="black", linewidth=2)
    plt.plot([105-16.5, 105-16.5], [13.84, 68-13.84], color="black", linewidth=2)
    plt.plot([0, 16.5], [13.84, 13.84], color="black", linewidth=2)
    plt.plot([0, 16.5], [68-13.84, 68-13.84], color="black", linewidth=2)
    plt.plot([105, 105-16.5], [13.84, 13.84], color="black", linewidth=2)
    plt.plot([105, 105-16.5], [68-13.84, 68-13.84], color="black", linewidth=2)
    centre_circle = plt.Circle((52.5, 34), 9.15, color="black", fill=False, linewidth=2)
    ax.add_patch(centre_circle)
    plt.scatter(52.5, 34, color="black", s=10)
    return fig, ax

# Page principale
def nation_page():
    st.title("Portail sélectionneur 🔍🌍")
    
    # Sélection de la nation
    nations = get_all_nations()

    col1, col2, col3 = st.columns(3)
    with col1: 
        nation = st.text_input("Rechercher un pays (en anglais)", "France")
    with col2 : 
        
        players_from_nation = get_players_by_nation(nation)
        
        # Sélection du poste
        positions = ["Tous les postes"] + sorted(players_from_nation['Position'].unique().tolist())

        selected_position = st.selectbox("Choisir un poste", options=positions)
    with col3:
        # Sélection de la plage de note
        ovr_range = st.slider(
            "Note générale des joueurs", 
            min_value=int(players_from_nation['OVR'].min()), 
            max_value=int(players_from_nation['OVR'].max()), 
            value=(int(players_from_nation['OVR'].min()), int(players_from_nation['OVR'].max())), 
            step=1
        )
        
    # Appliquer les filtres de position et de note
    if selected_position != "Tous les postes":
        filtered_df = players_from_nation[
            (players_from_nation['OVR'] >= ovr_range[0]) &
            (players_from_nation['OVR'] <= ovr_range[1]) &
            (players_from_nation['Position'] == selected_position)
        ]
    else:
        filtered_df = players_from_nation[
            (players_from_nation['OVR'] >= ovr_range[0]) &
            (players_from_nation['OVR'] <= ovr_range[1])
        ]
    
    # Calcul KPIs
    num_players = len(filtered_df)
    average_age = filtered_df['Age'].mean()
    average_OVR = filtered_df['OVR'].mean()

    # Drapeau & KPIs
    col0, col1, col2, col3 = st.columns(4)

    with col0:
        flag_url = get_flag_by_nation(nation)

        if flag_url and "Error" not in flag_url:
            st.image(flag_url)
        else:
            st.error(flag_url)

    with col1:
        st.metric("Nombre de joueurs", f"{num_players:.0f}")

    with col2:
        st.metric("Age moyen", f"{average_age:.0f}")

    with col3:
        st.metric("Note générale moyenne", f"{average_OVR:.0f}")
    
    # Afficher le terrain
    fig, ax = draw_pitch()
    
    # Position des différents postes
    position_coords = {
        "GK": (5, 34), "CB": (25, 34), "LB": (25, 10), "RB": (25, 58),
        "CDM": (40, 34), "LM": (50, 15), "RM": (50, 53), "LW": (75, 10),
        "RW": (75, 58), "ST": (95, 34), "CAM": (60, 34),
    }

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
    st.pyplot(fig)
    
    col1, col2 = st.columns(2)

    with col1:
        # Affichage d'un tableau avec les joueurs filtrés
        st.dataframe(filtered_df[['Name', 'Team', 'Position', 'OVR']])
    with col2: 
        # Affichage des championnats sous forme de graphique
        league_counts = filtered_df['League'].value_counts().reset_index()
        league_counts.columns = ['League', 'Number of Players']
        fig = px.pie(league_counts, names='League', values='Number of Players', hole=0.4, title="Top des championnats")
        st.plotly_chart(fig)

# Fonction pour exécuter l'application
nation_page()

