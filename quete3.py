import streamlit as st
import pandas as pd

# Configuration de la page
st.set_page_config(page_title="Cat Album Pro", layout="wide")

# 1. Chargement des données utilisateurs
def load_users():
    return pd.read_csv("users.csv")

def save_users(df):
    df.to_csv("users.csv", index=False)

# Initialisation du session_state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'username' not in st.session_state:
    st.session_state.username = None

# --- LOGIQUE D'AUTHENTIFICATION ---
def login():
    st.title("🔐 Connexion")
    with st.form("login_form"):
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        submit = st.form_submit_button("Se connecter")

        if submit:
            df = load_users()
            user_row = df[df['name'] == username]
            
            if not user_row.empty and user_row.iloc[0]['password'] == password:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success(f"Bienvenue {username} !")
                st.rerun()
            else:
                st.error("Identifiants incorrects")

# --- PAGES DE L'APPLICATION ---
def home_page():
    st.title("🏠 Accueil")
    st.write(f"Bienvenue sur votre espace sécurisé, **{st.session_state.username}**.")
    st.info("Utilisez le menu latéral pour naviguer vers l'album photo.")

def photo_album():
    st.title("🐱 Album de Chats")
    
    # Simulation d'une liste d'URLs d'images de chats
    cat_images = [f"https://placekitten.com/{200+i}/{200+i}" for i in range(9)]
    
    # Affichage en grille de 3 colonnes
    for i in range(0, len(cat_images), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(cat_images):
                cols[j].image(cat_images[i+j], use_container_width=True, caption=f"Chat n°{i+j+1}")

# --- GESTION DE LA NAVIGATION ---
if not st.session_state.authenticated:
    login()
else:
    # Sidebar
    st.sidebar.title("Navigation")
    st.sidebar.write(f"👤 **Bienvenue {st.session_state.username}**")
    
    page = st.sidebar.radio("Aller vers", ["Accueil", "Album Photo"])
    
    if st.sidebar.button("Déconnexion"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.rerun()

    # Rendu des pages
    if page == "Accueil":
        home_page()
    else:
        photo_album()