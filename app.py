import streamlit as st
import pandas as pd
import plotly.express as px
from pages.home import home_page
from pages.mercato import mercato_page
from pages.nation import nation_page
from pages.players import players_page
from pages.about_me import profile_page
# Load the datasets

if "df_players" not in st.session_state:
    st.session_state.df_players = pd.read_csv("./data/male_players.csv")


df_flags = pd.read_csv("./data/flags_iso.csv")  # Your country flags dataset