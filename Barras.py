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

# Grafico de Barras Novo:

graf_barras_novo = alt.Chart(fonte).mark_bar(
    cornerRadiusTopLeft = 10,
    cornerRadiusTopRight = 10

).encode(
    x = alt.X('a', sort = 'y'),
    y = 'b',
    #condicional para cores nas barras:
    color = alt.condition(
        alt.datum.b > 50,
        alt.value('steelblue'),# Se acima do valor, Azul
        alt.value('red')      # Se abaixo do valor, vermelho
    )
)

rotulo2 = graf_barras_novo.mark_text(
    align = 'center',
    baseline = 'middle',
    size = 14,
    dy = -15,
    

).encode(text = 'b')

# Inserindo linha media:

linha_media = alt.Chart(fonte).mark_rule(color = 'red').encode(
    y='mean(b)'
)

st.altair_chart(graf_barras_novo+rotulo2+linha_media, use_container_width = True)
