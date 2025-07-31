import streamlit as st
from PIL import Image
from model import predict

st.title("🖼️ Classificateur d’Images par IA")

uploaded_file = st.file_uploader("Télécharger une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image téléchargée", use_container_width=True)

    st.write("Classification en cours...")
    label = predict(image)
    st.success(f"Prédiction: **{label}**")

    
