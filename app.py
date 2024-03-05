import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Visualización de datos de anuncios de ventas de coches')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button = st.checkbox('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.checkbox("Construir gráfico de dispersión")
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(scatter, use_container_width=True)