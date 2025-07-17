import streamlit as st
import os

from openai import OpenAI

openai_api_key = ""

#client = OpenAI(api_key=openai_api_key)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Generador IA Profesional", layout="centered")

st.title("🧠 Generador de Contenido con IA")
st.write("Crea artículos, historias, correos y más con un prompt avanzado.")

# Selección del tipo de contenido
tipo = st.selectbox("Tipo de contenido", ["Artículo", "Historia", "Email", "Idea de negocio", "Post para redes sociales"])

tema = st.text_input("Tema o idea principal", placeholder="Ej: Inteligencia Artificial en educación")
tono = st.selectbox("Tono del texto", ["Profesional", "Creativo", "Informal", "Persuasivo", "Divertido"])
publico = st.text_input("Público objetivo", placeholder="Ej: docentes universitarios, jóvenes emprendedores")
extension = st.selectbox("Extensión aproximada", ["Corto (100-200 palabras)", "Medio (300-500)", "Largo (600-1000)"])

if st.button("Generar"):
    if not tema:
        st.warning("Por favor ingresa un tema.")
    else:
        with st.spinner("Generando contenido..."):
            prompt = f"""
Eres un experto redactor con años de experiencia. Genera un {tipo.lower()} de alta calidad sobre el tema: "{tema}".
Debe tener:
- Tono: {tono.lower()}
- Público objetivo: {publico}
- Extensión aproximada: {extension}
            """

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8,
                max_tokens=800
            )

            generated_text = response.choices[0].message.content
            st.success(f"{tipo} generado:")
            st.write(generated_text)