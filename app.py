import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(r'C:\Users\luisP\Downloads\Sprint-5-project\vehicles_us.csv')
fig = px.histogram(car_data, x="odometer") # crear un histograma
fig.show()