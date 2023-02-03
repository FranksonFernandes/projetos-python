import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv('./dados/vega_car.csv')

graf_dispersao = alt.Chart(df).mark_point().encode(
    x = 'Horsepower:Q',  # ":Q" Medida Quantitativa
    y = 'Miles_per_Gallon',
    color = alt.Color('Origin:N') # 'N': Nominal
)

st.subheader('Gráfico de Dispersão: Consumo por Cavalo')
st.altair_chart(graf_dispersao, use_container_width = True)