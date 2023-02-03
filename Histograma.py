import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_excel(
    io = 'dados/normal_dist.xlsx',
    engine = 'openpyxl',
    sheet_name = 'Sheet1',
    usecols = 'A:C',
    nrows =87,
)

Histograma = alt.Chart(df).mark_bar().encode(
    x = alt.X('x', bin=alt.Bin(step = 10)),
    y = 'sum(count)'
) 

st.subheader('Histograma: Notas de Mil alunos (Agrupados de 10 em 10)')

st.altair_chart(Histograma, use_container_width = True)