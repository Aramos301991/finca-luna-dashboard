import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="Finca Luna Nueva Lodge - Miami Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título y descripción
st.title("🌿 Finca Luna Nueva Lodge - Expansión a Miami")
st.markdown("""
Dashboard interactivo para analizar la viabilidad de la expansión del hotel ecológico en Miami.
""")

# --- Datos (simulados basados en el documento) ---
@st.cache_data
def load_data():
    # Datos de inventario hotelero (2023-2025)
    hotel_inventory = pd.DataFrame({
        "Año": [2023, 2024, 2025],
        "Habitaciones": [67881, 71600, 75500]
    })

    # Distribución por submercado (2025)
    market_distribution = pd.DataFrame({
        "Zona": ["Miami Beach", "Downtown/Brickell", "Otras"],
        "Porcentaje": [38.5, 30.0, 31.5]  # Estimado
    })

    # Rendimiento hotelero (2025)
    performance = pd.DataFrame({
        "Métrica": ["Ocupación", "Tarifa Diaria Promedio (USD)", "RevPAR (USD)"],
        "Valor": [71.6, 220.48, 157.91]
    })

    # Visitantes a Miami (2023)
    visitors = pd.DataFrame({
        "Tipo": ["Nocturnos", "Internacionales", "Nacionales", "Residentes FL"],
        "Millones": [19.298, 4.905, 10.031, 4.362]
    })

    return hotel_inventory, market_distribution, performance, visitors

hotel_inventory, market_distribution, performance, visitors = load_data()

# --- Sidebar (filtros) ---
st.sidebar.header("Filtros")
selected_year = st.sidebar.selectbox("Año de análisis", [2023, 2024, 2025])

# --- Sección 1: Mercado Hotelero ---
st.header("📊 Mercado Hotelero en Miami")

# Gráfico 1: Inventario de habitaciones (2023-2025)
fig1 = px.bar(
    hotel_inventory,
    x="Año",
    y="Habitaciones",
    title="Inventario Total de Habitaciones (2023-2025)",
    color="Año",
    labels={"Habitaciones": "Total de Habitaciones"}
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Distribución por submercado (2025)
fig2 = px.pie(
    market_distribution,
    names="Zona",
    values="Porcentaje",
    title="Distribución del Mercado Hotelero por Zona (2025)"
)
st.plotly_chart(fig2, use_container_width=True)

# --- Sección 2: Rendimiento y Visitantes ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Rendimiento Hotelero (2025)")
    st.dataframe(performance, hide_index=True)

with col2:
    st.subheader("Visitantes a Miami (2023)")
    fig3 = px.bar(
        visitors,
        x="Tipo",
        y="Millones",
        title="Turistas por Tipo (Millones)",
        color="Tipo"
    )
    st.plotly_chart(fig3, use_container_width=True)

# --- Sección 3: Financiamiento y Segmentación ---
st.header("💰 Financiamiento y Clientes")

# Tasas de interés
interest_rates = pd.DataFrame({
    "Fuente": ["Bancos Privados", "USDA (Préstamos Agrícolas)"],
    "Tasa (%)": [6.5, 4.75]
})

st.subheader("Tasas de Interés para Préstamos")
st.dataframe(interest_rates, hide_index=True)

# Segmentación de clientes
st.subheader("Perfil del Cliente Objetivo")
client_profile = {
    "Edad": "25-55 años",
    "Ingresos Anuales": "≥ $50,000 USD",
    "Intereses": "Turismo sostenible, bienestar, naturaleza",
    "Tarifa Promedio/Noche": "$90-$250 USD"
}
st.json(client_profile)

# --- Sección 4: Estrategias de Marketing ---
st.header("📢 Estrategias de Marketing")

# ROI por red social (datos simulados)
roi_data = pd.DataFrame({
    "Red Social": ["YouTube", "Instagram", "TikTok", "LinkedIn"],
    "ROI (%)": [25, 18, 15, 8],
    "Ingresos Generados (USD)": [320000, 350000, 165000, 120000]
})

st.subheader("ROI por Red Social (2025)")
fig4 = px.bar(
    roi_data,
    x="Red Social",
    y="ROI (%)",
    color="Red Social",
    title="Retorno de Inversión (ROI) por Plataforma"
)
st.plotly_chart(fig4, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.caption("Dashboard creado para el plan de mercadeo de Finca Luna Nueva Lodge en Miami (2025)")
