import streamlit as st
import openai
import os

# Cargar clave API desde variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Generador de Texto IA ✨")
prompt = st.text_area("Introduce un prompt para la IA:")

if st.button("Generar"):
    if prompt.strip() == "":
        st.warning("Por favor, escribe un prompt.")
    else:
        with st.spinner("Generando..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )
            st.success("Texto generado:")
            st.write(response['choices'][0]['message']['content'])
