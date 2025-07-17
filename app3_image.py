import streamlit as st
import os
from openai import OpenAI

# Carga tu clave API de OpenAI
openai_api_key = ""

#client = OpenAI(api_key=openai_api_key)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
 
st.set_page_config(page_title="Generador de Imágenes con IA", layout="centered")

st.title("🎨 Generador de Imágenes con IA")
st.markdown("Escribe una descripción y genera una imagen usando IA (DALL·E).")

# Prompt del usuario
prompt = st.text_input("Describe la imagen que deseas generar", placeholder="Un castillo en la luna iluminado por estrellas fugaces")

# Tamaño de imagen
size = st.selectbox("Tamaño de imagen", ["1024x1024", "1024x1792", "1792x1024"])

# Botón de generar
if st.button("🎨 Generar Imagen"):
    if not prompt.strip():
        st.warning("Por favor, escribe un prompt.")
    else:
        with st.spinner("Generando imagen..."):
            try:
                response = client.images.generate(
                    prompt=prompt,
                    n=1,
                    size=size,
                    model="dall-e-3"  # o "dall-e-2"
                )
                image_url = response.data[0].url
                st.image(image_url, caption="Imagen generada", use_column_width=True)
                st.markdown(f"[📥 Descargar imagen]({image_url})")
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
