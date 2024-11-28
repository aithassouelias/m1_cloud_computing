import streamlit as st
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

st.set_page_config(page_title="Portail joueurs", page_icon="📊")

df_players = pd.read_csv("./data/male_players.csv")

st.title("Player Statistics")
st.write("Explore player statistics and find similar profiles using machine learning.")

# Colonnes pertinentes pour la similarité
features = [
'OVR', 'PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY',
'Acceleration', 'Sprint Speed', 'Positioning', 'Finishing', 'Shot Power',
'Long Shots', 'Volleys', 'Penalties', 'Vision', 'Crossing', 'Free Kick Accuracy',
'Short Passing', 'Long Passing', 'Curve', 'Dribbling', 'Agility', 'Balance',
'Reactions', 'Ball Control', 'Composure', 'Interceptions', 'Heading Accuracy',
'Def Awareness', 'Standing Tackle', 'Sliding Tackle', 'Jumping', 'Stamina',
'Strength', 'Aggression'
]

# Filtrer les données sur les features pertinentes
X = df_players[features]

# Normalisation
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Modèle KNN
knn = NearestNeighbors(n_neighbors=6, metric='euclidean')  # n_neighbors=6 pour exclure le joueur lui-même
knn.fit(X_scaled)

player_name = st.text_input("Entrez le nom du joueur pour trouver des profils similaires :", "")

if player_name:
    # Recherche du joueur dans les données
    selected_player = df_players[df_players['Name'].str.contains(player_name, case=False, na=False)]

    if not selected_player.empty:
        player_features = selected_player[features].values
        player_scaled = scaler.transform(player_features)

        # Trouver les joueurs les plus proches
        distances, indices = knn.kneighbors(player_scaled)
        similar_players = df_players.iloc[indices[0]]

        # Exclure le joueur lui-même des résultats
        similar_players = similar_players[similar_players['Name'] != player_name]
        similarity_scores = 1 - distances[0][1:] / distances[0][1:].max()  # Normaliser les distances en scores

        # Ajouter les scores de similarité à la dataframe
        similar_players = similar_players.copy()
        similar_players['Similarity (%)'] = (similarity_scores * 100).round(2)

        # Préparer la table avec les liens cliquables
        display_df = similar_players[['Name', 'Team', 'Position', 'OVR', 'Similarity (%)', 'url']]
        
        display_df.drop(columns=['url'], inplace=True)

        # Configuration AgGrid pour les liens cliquables
        gb = GridOptionsBuilder.from_dataframe(display_df)
        gb.configure_column("Name", cellRenderer="html")
        grid_options = gb.build()

        # Afficher la table interactive
        st.write(f"Joueurs similaires à **{player_name}** :")
        AgGrid(display_df, gridOptions=grid_options, enable_enterprise_modules=False, height=300)
        # Affichage radar chart
        target_player = similar_players.iloc[0]  # Premier joueur similaire
        radar_features = [f for f in features if len(f) == 3]  # Features avec 3 caractères

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=selected_player[radar_features].values[0],
            theta=radar_features,
            fill='toself',
            name=player_name
        ))
        fig.add_trace(go.Scatterpolar(
            r=target_player[radar_features].values,
            theta=radar_features,
            fill='toself',
            name=target_player['Name']
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100])
            ),
            showlegend=True,
            title="Comparaison des caractéristiques (Features avec 3 caractères)"
        )

        st.plotly_chart(fig)
    else:
        st.write(f"Aucun joueur trouvé pour le nom : {player_name}")
            

       