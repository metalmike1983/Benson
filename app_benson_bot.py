
import streamlit as st
import json
import random

# Carica dataset
with open("benson_chatbot_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Funzione per trovare risposta
def get_benson_response(user_input):
    for item in data:
        if item["trigger"] in user_input.lower():
            return random.choice(item["responses"])
    return random.choice([
        "Non ho capito... ripeti meglio, magari urlando!",
        "Sei confuso come un fonico con l'otite!",
        "Avete capito?! Domande più chiare, per favore!"
    ])

# UI Streamlit
st.set_page_config(page_title="Richard Benson Bot", page_icon="🎸")
st.title("🎸 Richard Benson Chatbot")
st.markdown("**Parla con il maestro del metallo!** Fai una domanda o scrivi una parola chiave (es. saluto, elogio, politica, metal...)")

user_input = st.text_input("Cosa vuoi chiedere a Richard Benson?")

if user_input:
    response = get_benson_response(user_input)
    st.markdown(f"**Richard Benson dice:** _{response}_")

if st.button("🎲 Frase casuale alla Benson"):
    random_entry = random.choice(data)
    st.markdown(f"**Frase casuale:** _{random.choice(random_entry['responses'])}_")
