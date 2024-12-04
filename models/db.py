import pyodbc
import os
import pandas as pd


# Configuration de la connexion à la base de données
def connect_db():
    db_host = os.getenv("DB_HOST") 
    db_name = os.getenv("DB_NAME")  
    db_user = os.getenv("DB_USER")  
    db_password = os.getenv("DB_PASSWORD")
    connection_string = (
        f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={db_host};DATABASE={db_name};UID={db_user};PWD={db_password}'
    )

    # Connexion à SQL Server
    conn = pyodbc.connect(connection_string)
    return conn

# Récupérer les joueurs d'une nation
def get_players_by_nation(nation="France"):
    conn = connect_db()
    query = """
    SELECT * FROM players_table
    WHERE Nation = ?;
    """
    # Utilisation de paramètres liés
    df = pd.read_sql(query, conn, params=(nation,))
    conn.close()
    return df

# Récupérer les informations de drapeau
def get_flag_by_nation(nation="France"):
    conn = connect_db()
    query = "SELECT URL FROM flags_table WHERE Country = ?;"
    try:
        df = pd.read_sql(query, conn, params=(nation,))
        conn.close()
        if df.empty:
            return f"No flag found for nation: {nation}"
        return df['URL'].iloc[0]
    except Exception as e:
        conn.close()
        return f"Error occurred: {e}"


# Récupérer toutes les nations disponibles
def get_all_nations():
    conn = connect_db()
    query = """
    SELECT DISTINCT Nation FROM players_table;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df['Nation'].tolist()

# Récupérer toutes les données des joueurs depuis la BDD
def get_players_data():
    conn = connect_db()
    query = """SELECT Name, Team, Position, OVR, PAC, SHO, PAS, DRI, DEF, PHY,
        Acceleration, Sprint_Speed, Positioning, Finishing, Shot_Power,
        Long_Shots, Volleys, Penalties, Vision, Crossing, Free_Kick_Accuracy,
        Short_Passing, Long_Passing, Curve, Dribbling, Agility, Balance,
        Reactions, Ball_Control, Composure, Interceptions, Heading_Accuracy,
        Def_Awareness, Standing_Tackle, Sliding_Tackle, Jumping, Stamina,
        Strength, Aggression FROM players_table"""
    df = pd.read_sql(query, conn)
    conn.close()
    return df
