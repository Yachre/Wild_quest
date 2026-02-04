import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'cuihuahuynh@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "root",         # Le nom du cookie, un str quelconque
    "root",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)


def accueil():
      st.title("Bienvenu ")


with st.sidebar:
    selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )
    

    if st.session_state["authentication_status"]:
        accueil()
    # Le bouton de déconnexion
    authenticator.logout("Déconnexion")
    # On indique au programme quoi faire en fonction du choix

if selection == "Accueil":
    st.header("Bienvenue ma page d'accueil !")
elif selection == "Photos":
    st.header("Bienvenue sur l'album photo de Bowie")

# Création de 3 colonnes 
    col1, col2, col3 = st.columns(3)

# Contenu de la première colonne : 
    with col1:
        st.image("https://s1.qwant.com/thumbr/474x315/0/5/303f9bcdaf8e4f737824b80abbcc2e9163cc52aa596eca813968bb102e97fa/OIP.sBUaw-vCcNrf6z-8yyQ_7wHaE7.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%2Fid%2FOIP.sBUaw-vCcNrf6z-8yyQ_7wHaE7%3Fpid%3DApi&q=0&b=1&p=0&a=0")

# Contenu de la deuxième colonne :
    with col2:
        st.image("https://s2.qwant.com/thumbr/474x316/7/8/d84f01cad9fca0744a14b1bc2135975d96ca41d588def6f8d9dd63fd365b19/OIP.ZVTQ0Ikd_ncXxmWcGH5P5QHaE8.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%2Fid%2FOIP.ZVTQ0Ikd_ncXxmWcGH5P5QHaE8%3Fpid%3DApi&q=0&b=1&p=0&a=0")

# Contenu de la troisième colonne : 
    with col3:
        st.image("https://s1.qwant.com/thumbr/474x316/0/0/6ca268f16c601a77f8c0bb76cf8e0ea2740c69dc65a57025982d74e6fec1ea/OIP.9LG-t-YtgSQU8CMjM3UwRQHaE8.jpg?u=https%3A%2F%2Ftse.mm.bing.net%2Fth%2Fid%2FOIP.9LG-t-YtgSQU8CMjM3UwRQHaE8%3Fcb%3Ddefcachec2%26pid%3DApi&q=0&b=1&p=0&a=0")

