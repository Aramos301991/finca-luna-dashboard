import streamlit as st
import sys
import subprocess
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

def install_packages():
    required = ["pandas==2.2.1", "plotly==5.18.0", "numpy==1.26.0"]
    for package in required:
        try:
            __import__(package.split('==')[0])
            logging.info(f"{package} ya está instalado")
        except ImportError:
            logging.info(f"Instalando {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_packages()

# Ahora importa las librerías
import pandas as pd
import plotly.express as px
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="Finca Luna Nueva Lodge - Miami",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título
st.title("🌿 Finca Luna Nueva Lodge - Dashboard de Expansión")
st.markdown("Análisis de mercado, financiamiento y estrategias para Miami.")

# --- Carga de datos desde CSV (cacheados) ---
@st.cache_data
def load_data():
    mercado_hotelero = pd.read_csv("mercado_hotelero.csv")
    submercados = pd.read_csv("submercados.csv")
    visitantes = pd.read_csv("visitantes.csv")
    financiamiento = pd.read_csv("financiamiento.csv")
    marketing_roi = pd.read_csv("marketing_roi.csv")
    return mercado_hotelero, submercados, visitantes, financiamiento, marketing_roi

mercado_hotelero, submercados, visitantes, financiamiento, marketing_roi = load_data()

# --- Sección 1: Mercado Hotelero ---
st.header("📊 Mercado Hotelero en Miami")

# Gráfico de inventario de habitaciones
fig1 = px.bar(
    mercado_hotelero,
    x="Año",
    y="Habitaciones",
    title="Inventario de Habitaciones (2023-2025)",
    color="Año"
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico de distribución por submercado
fig2 = px.pie(
    submercados,
    names="Zona",
    values="Porcentaje",
    title="Distribución por Zona (2025)"
)
st.plotly_chart(fig2, use_container_width=True)

# --- Sección 2: Visitantes y Financiamiento ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Visitantes a Miami (2023)")
    fig3 = px.bar(
        visitantes,
        x="Tipo",
        y="Millones",
        color="Tipo",
        title="Turistas por Tipo"
    )
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("Opciones de Financiamiento")
    st.dataframe(financiamiento, hide_index=True)

# --- Sección 3: Marketing ---
st.header("📈 Estrategias de Marketing")

# ROI por red social
fig4 = px.bar(
    marketing_roi,
    x="Red Social",
    y="ROI (%)",
    color="Red Social",
    title="Retorno de Inversión por Plataforma"
)
st.plotly_chart(fig4, use_container_width=True)

# --- Sección 4: Datos en Tablas ---
with st.expander("🔍 Ver todos los datos"):
    st.subheader("Mercado Hotelero")
    st.dataframe(mercado_hotelero, hide_index=True)
    
    st.subheader("Visitantes")
    st.dataframe(visitantes, hide_index=True)

# --- Footer ---
st.markdown("---")
st.caption("Dashboard creado para el plan de expansión de Finca Luna Nueva Lodge (2025)")
