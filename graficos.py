import altair as alt
import pandas as pd
import streamlit as st


# Criando um Data Frame como exemplo:

fonte = pd.DataFrame({

    'a':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b':[28,55,43,91, 81, 53, 19, 87, 52]
})

# Desenvolvendo um grafico de barras:

graf_barras = alt.Chart(fonte).mark_bar().encode(
    x = 'a',
    y = 'b',
    color = 'a',
    tooltip = ['a','b']
)

# Inserindo Rótulo nas barras:
rotulo = graf_barras.mark_text(
    dy = -6,
    size = 17
    ).encode(text = 'b',)

st.subheader('Gráfico de Barras')
#Plotando o Gráfico:
st.altair_chart(graf_barras+rotulo, use_container_width = True)

#-------------- Fim Gráfico Barras------------------------

# Desenvolvedo Gráfico de Área:
st.subheader('Gráfico de Área')
graf_area = alt.Chart(fonte).mark_area(
    color = 'lightblue',
    interpolate = 'step-after',
    line = True
).encode(x = 'a', y = 'b', tooltip = ['a', 'b'])

rotulo_area = graf_area.mark_text(

    dy = -8,
    dx = 30,
    size = 17,
    color = 'white'
).encode(text = 'b')

st.altair_chart(graf_area+rotulo_area, use_container_width = True)

#-------------- Fim Gráfico Área ------------------------

# Desenvolvedo Gráfico de Pizza (Setores):

st.subheader('Gráfico de Pizza')

graf_pizza = alt.Chart(fonte).mark_arc().encode(
    theta = alt.Theta(field = 'b', type = 'quantitative'),
    color = alt.Color(field = 'a', type = 'nominal')
)

st.altair_chart(graf_pizza)


