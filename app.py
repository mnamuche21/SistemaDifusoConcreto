import streamlit as st
from logica.sistema import evaluar


st.set_page_config(
    page_title="Predicción de Resistencia del Concreto",
    page_icon="🏗️"
)


st.title("Predicción de Resistencia del Concreto")
st.write("Sistema difuso para estimar resistencia a compresión")


cemento = st.number_input(
    "Cemento (kg/m³)",
    min_value=0.0
)

agua = st.number_input(
    "Agua (kg/m³)",
    min_value=0.0
)

superplastificante = st.number_input(
    "Superplastificante (kg/m³)",
    min_value=0.0
)

fino = st.number_input(
    "Agregado fino (kg/m³)",
    min_value=0.0
)

edad = st.number_input(
    "Edad del concreto (días)",
    min_value=1.0
)


if st.button("Calcular resistencia"):

    try:

        resistencia = evaluar(
            cemento,
            agua,
            superplastificante,
            fino,
            edad
        )

        st.success(
            f"Resistencia estimada: {resistencia:.2f} MPa"
        )

    except Exception as e:

        st.error("Error al calcular")
        st.write(e)
