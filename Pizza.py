import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_excel(
    io = 'dados/faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name = 'ricos',
    usecols = 'A:B',
    nrows =9
)

st.subheader('Gráfico de Pizza')

graf_pizza = alt.Chart(df).mark_arc(

    innerRadius = 0,
    outerRadius = 150 # Tamanho do Gráfico
    
).encode(
    theta = alt.Theta(field = 'Fortuna',
    type = 'quantitative',
    stack = True),
    color = alt.Color(
    field = 'Nome',
    type = 'nominal',
    legend = None), # <- Retira legenda
    tooltip = ['Nome', 'Fortuna']
).properties(width = 800, height = 500) # Configurando a área do Grafico 

rotuloNome = graf_pizza.mark_text(radius = 210, size = 15).encode(text = 'Nome')
rotuloValor = graf_pizza.mark_text(radius = 170, size = 15).encode(text = 'Fortuna')

st.altair_chart(graf_pizza + rotuloNome + rotuloValor)