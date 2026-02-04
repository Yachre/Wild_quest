import streamlit as st
from streamlit_option_menu import option_menu

# --- 1. CONFIGURATION ET DONNÉES ---
st.set_page_config(page_title="Bowie Album", layout="wide")

# Votre dictionnaire de données
lesDonneesDesComptes = {
    'root': {
        'name': 'root',
        'password': 'root',
        'email': 'cuihuahuynh@gmail.com',
        'failed_login_attempts': 0,
        'logged_in': False,
        'role': 'administrateur'
    },
    'user1': {
        'name': 'Bowie',
        'password': 'FAN',
        'email': 'fan@exemple.com',
        'failed_login_attempts': 0,
        'logged_in': False,
        'role': 'membre'
    }
}

# Initialisation de la session
if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'user' not in st.session_state:
    st.session_state.user = None

# --- 2. FONCTION DE CONNEXION ---
def login():
    st.title("🔐 Connexion")
    user_input = st.text_input("Nom d'utilisateur")
    pass_input = st.text_input("Mot de passe", type="password")
    
    if st.button("Se connecter"):
        # On vérifie si l'utilisateur existe dans les clés du dictionnaire
        if user_input in lesDonneesDesComptes:
            if lesDonneesDesComptes[user_input]['password'] == pass_input:
                st.session_state.auth = True
                st.session_state.user = lesDonneesDesComptes[user_input]['name']
                st.rerun()
            else:
                st.error("Mot de passe incorrect")
        else:
            st.error("Utilisateur inconnu")

# --- 3. INTERFACE PRINCIPALE ---
if not st.session_state.auth:
    login()
else:
    # Sidebar
    with st.sidebar:
        st.success(f"Bienvenue **{st.session_state.user}**")
        
        selection = option_menu(
            menu_title="Menu",
            options=["Accueil", "Photos"],
            icons=["house", "camera"],
            default_index=0,
        )
        
        st.markdown("---")
        if st.button("Déconnexion"):
            st.session_state.auth = False
            st.session_state.user = None
            st.rerun()

    # Logique des pages
    if selection == "Accueil":
        st.header("Bienvenue sur ma page d'accueil !")
        st.write("Ceci est un espace sécurisé géré par un dictionnaire Python.")
        st.image("https://s2.qwant.com/thumbr/474x315/e/7/66d15e9bc1d680790ae2cbe406b5e65d39c4aa2cfdb634bcd453e9bca9649e/OIP.-yDi2WsnPnI4JRXj2equmAHaE7.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%2Fid%2FOIP.-yDi2WsnPnI4JRXj2equmAHaE7%3Fpid%3DApi&q=0&b=1&p=0&a=0")

    elif selection == "Photos":
        st.header("🐱 Album photo de Bowie")
        
        # Liste des images
        urls = [
            "https://s1.qwant.com/thumbr/474x315/0/5/303f9bcdaf8e4f737824b80abbcc2e9163cc52aa596eca813968bb102e97fa/OIP.sBUaw-vCcNrf6z-8yyQ_7wHaE7.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%2Fid%2FOIP.sBUaw-vCcNrf6z-8yyQ_7wHaE7%3Fpid%3DApi&q=0&b=1&p=0&a=0",
            "https://s2.qwant.com/thumbr/474x316/7/8/d84f01cad9fca0744a14b1bc2135975d96ca41d588def6f8d9dd63fd365b19/OIP.ZVTQ0Ikd_ncXxmWcGH5P5QHaE8.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%2Fid%2FOIP.ZVTQ0Ikd_ncXxmWcGH5P5QHaE8%3Fpid%3DApi&q=0&b=1&p=0&a=0",
            "https://s1.qwant.com/thumbr/474x316/0/0/6ca268f16c601a77f8c0bb76cf8e0ea2740c69dc65a57025982d74e6fec1ea/OIP.9LG-t-YtgSQU8CMjM3UwRQHaE8.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%2Fid%2FOIP.9LG-t-YtgSQU8CMjM3UwRQHaE8%3Fcb%3Ddefcachec2%26pid%3DApi&q=0&b=1&p=0&a=0"
        ]

        # Disposition 3 images par ligne
        cols = st.columns(3)
        for i in range(3):
            with cols[i]:
                st.image(urls[i], use_container_width=True, caption=f"Bowie {i+1}")