import streamlit as st
import json

# --- Function to load JSON data ---
def load_json_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

# --- Load all data ---
def load_data():
    data = {
        "livres": load_json_data("database/books.json"),
        "magazines": load_json_data("database/magazine.json"),
        "journaux": load_json_data("database/newspaper.json"),
        "multimedias": load_json_data("database/disk.json"),
    }
    return data

# --- Streamlit App ---
st.title("Bibliothèque d'Ohara")

# Initialize session state for selected item
if "selected_item" not in st.session_state:
    st.session_state.selected_item = None

# Load the data
bibliotheque = load_data()

# Function to select an item
def select_item(item):
    st.session_state.selected_item = item

# Function to reset selected item
def reset_selection():
    st.session_state.selected_item = None

# Display item details if one is selected
if st.session_state.selected_item:
    item = st.session_state.selected_item
    st.header(f"Détails de {item['titre']}")
    if "auteur" in item:
        st.write(f"**Auteur**: {item['auteur']}")
    if "pages" in item:
        st.write(f"**Pages**: {item['pages']}")
    if "genre" in item:
        st.write(f"**Genre**: {item['genre']}")
    if "id" in item:
        st.write(f"**UUID**: {item['id']}")
    if "editeur" in item:
        st.write(f"**Éditeur**: {item['editeur']}")
    if "frequence" in item:
        st.write(f"**Fréquence**: {item['frequence']}")
    if "date_publication" in item:
        st.write(f"**Date de Publication**: {item['date_publication']}")
    if "duree_totale" in item:
        st.write(f"**Durée Totale**: {item['duree_totale']}")

    # Button to return to the list
    st.button("Retour à la Liste", on_click=reset_selection)
else:
    # Category selection
    categorie = st.selectbox(
        "Choisissez une catégorie à explorer",
        ["Livres", "Magazines", "Journaux", "Ouvrages Multimédias"]
    )

    # Display the list of items for the selected category
    if categorie == "Livres":
        st.header("Catalogue des Livres")
        for livre in bibliotheque["livres"]:
            st.button(
                livre["titre"], 
                key=f"livre_{livre['id']}", 
                on_click=select_item, 
                args=(livre,)
            )

    elif categorie == "Magazines":
        st.header("Catalogue des Magazines")
        for magazine in bibliotheque["magazines"]:
            st.button(
                magazine["titre"], 
                key=f"magazine_{magazine['uuid']}", 
                on_click=select_item, 
                args=(magazine,)
            )

    elif categorie == "Journaux":
        st.header("Catalogue des Journaux")
        for journal in bibliotheque["journaux"]:
            st.button(
                journal["titre"], 
                key=f"journal_{journal['uuid']}", 
                on_click=select_item, 
                args=(journal,)
            )

    elif categorie == "Ouvrages Multimédias":
        st.header("Catalogue des Ouvrages Multimédias")
        for multimedia in bibliotheque["multimedias"]:
            st.button(
                multimedia["titre"], 
                key=f"multimedia_{multimedia['uuid']}", 
                on_click=select_item, 
                args=(multimedia,)
            )
