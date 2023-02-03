import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_excel(
    io = 'dados/faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name = 'flow',
    usecols = 'A:B',
    nrows =15,
)

graf_dados = alt.Chart(df).mark_area(

  color = 'green',
  line = {'color' : 'black'}

).encode(
    x = 'Year:T',
    y = 'Value:Q'
)

rotulo = graf_dados.mark_text(
    size = 14,
    color = 'white',
    align = 'center',
    dy = -15
).encode(text = 'Value')


st.subheader('Gráfico de Área: Resultados Anuais')
st.altair_chart(graf_dados + rotulo, use_container_width = True)
