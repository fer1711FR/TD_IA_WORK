import streamlit as st
import os

from openai import OpenAI

# openai_api_key = ""

#client = OpenAI(api_key=openai_api_key)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Generador de Texto IA ✨")
prompt = st.text_area("Introduce un prompt para la IA:")

if st.button("Generar"):
    if prompt.strip() == "":
        st.warning("Por favor, escribe un prompt.")
    else:
        with st.spinner("Generando..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hola"}]
            )
            st.success("Texto generado:")
            # st.write(response['choices'][0]['message']['content'])
            st.write(response.choices[0].message.content)
