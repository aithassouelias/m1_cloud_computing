import streamlit as st
import importlib

# Configuration globale de la page
st.set_page_config(page_title="TalentTracker", page_icon="🎯", layout="wide")

# Dictionnaire pour mapper les noms de pages aux modules Python
PAGES = {
    "🏠 Accueil": "my_pages.home",
    "📊 Portail Sélectionneur": "my_pages.nation",
    "🎯 Statistiques joueurs": "my_pages.players",
    "ℹ️ À propos de moi": "my_pages.about_me",
}

# Affichage des options sous forme de boutons radio
selected_page = st.sidebar.radio("", list(PAGES.keys()))

# Chargement dynamique du module correspondant
try:
    page_module = importlib.import_module(PAGES[selected_page])
    page_module.run() 
except ModuleNotFoundError:
    st.error(f"Erreur : Impossible de charger la page '{selected_page}'")
