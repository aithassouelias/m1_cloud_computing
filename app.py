import streamlit as st
import pandas as pd
import plotly.express as px
from pages.home import home_page
from pages.mercato import mercato_page
from pages.nation import nation_page
from pages.players import players_page
from pages.about_me import profile_page
# Load the datasets
df_players = pd.read_csv("./data/male_players.csv")  # Your football players dataset
df_flags = pd.read_csv("./data/flags_iso.csv")  # Your country flags dataset

# Create the main navigation bar in the sidebar
page = st.sidebar.selectbox("Select a Page", ("Page d'accueil", "Portail séléctionneur", "Portail Mercato", "Joueurs","A propos de moi"))

# Display the appropriate page based on the selection
if page == "Page d'accueil":
    home_page()
elif page == "Portail séléctionneur":
    nation_page(df_players, df_flags)
elif page == "Portail Mercato":
    mercato_page()
elif page == "Joueurs":
    players_page(df_players)
elif page == "A propos de moi":
    profile_page()
