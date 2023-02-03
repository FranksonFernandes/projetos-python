import streamlit as st
import pandas as pd
import altair as alt


# Configuração da Página:
st.set_page_config(
    page_title = 'DASHBOARD DE VENDAS',
    layout = 'wide',

)

# Importando data Frame
df = pd.read_excel(
    io = 'dados/system_extraction.xlsx',
    engine = 'openpyxl',
    sheet_name = 'salesreport',
    usecols = 'A:J',
    nrows =4400,
)

# Criar sidebar (Filtros)
  
with st.sidebar:
    st.subheader('Dashboad de Vendas')
    fVendedor = st.selectbox(
        "Selecione o Vendedor",
        options = df['Vendedor'].unique()
    )

    fProduto = st.selectbox(
        "Selecione o Produto:",
        options = df['Produto vendido'].unique()
    )

    fCliente = st.selectbox(
        "Selecione o Cliente:",
        options = df['Cliente'].unique()
    )

# Tabela qtde vendida por produto
tab1_qdt_produto = df.loc[(df['Vendedor'] == fVendedor) & (df['Cliente'] == fCliente)]

tab1_qdt_produto = tab1_qdt_produto.groupby('Produto vendido').sum().reset_index()  

#Tabela de Vendas e Margem de Lucro
tab2_vendas_margem = df.loc[(
    df['Vendedor'] == fVendedor) &
   (df['Produto vendido'] == fProduto) &
   (df['Cliente'] == fCliente) 
] 

# Tabela de Vendas por Vendedor
tab3_Vendas_Vendedor = df.loc[
    (df['Produto vendido'] == fProduto) &
    (df['Cliente'] == fCliente)
]

tab3_Vendas_Vendedor = tab3_Vendas_Vendedor.groupby('Vendedor').sum().reset_index()
tab3_Vendas_Vendedor = tab3_Vendas_Vendedor.drop(columns = ['Nº pedido', 'Preço']) 

#Tabela Vendas por Cliente
tab4_Venda_Cliente = df.loc[
    (df['Vendedor'] == fVendedor) &
    (df['Produto vendido'] == fProduto)
]

tab4_Venda_Cliente = tab4_Venda_Cliente.groupby('Cliente').sum().reset_index()

#Tabela Vendas Mensais

tab5_Vendas_Mensais = df.loc[
    (df['Vendedor'] == fVendedor) &
    (df['Produto vendido'] == fProduto) &
    (df['Cliente'] == fCliente)
]

#Formatando a data
tab5_Vendas_Mensais['mm'] = tab5_Vendas_Mensais['Data'].dt.strftime('%m/%Y')


#------------------------------- Gráficos -------------------------------------#
cor_grafico = 'cor aqui'
altura_grafico = 250

# Gráfico 1.0 qtde vendida por produto:

graf1_qtd_produto = alt.Chart(tab1_qdt_produto).mark_bar(
    #color = cor_grafico,
    cornerRadiusTopLeft = 9,
    cornerRadiusTopRight = 9
).encode(
    x = 'Produto vendido',
    y = 'Quantidade',
    tooltip = ['Produto vendido','Quantidade']
).properties(height = altura_grafico, title = 'QUANTIDADE VENDIDA POR PRODUTO').configure_axis(grid = False).configure_view(strokeWidth = 0)

# Gráfico 1.1 Valor da venda por produto:

graf1_valor_produto = alt.Chart(tab1_qdt_produto).mark_bar(
    #color = cor_grafico,
    cornerRadiusTopLeft = 9,
    cornerRadiusTopRight = 9
).encode(
    x = 'Produto vendido',
    y = 'Quantidade',
    tooltip = ['Produto vendido','Valor Pedido']
).properties(height = altura_grafico, title = 'VALOR TOTAL POR PRODUTO').configure_axis(grid = False).configure_view(strokeWidth = 0)


#Grafico de Vendas por Vendedor (Pizza):

graf2_Vendas_Vendedor = alt.Chart(tab3_Vendas_Vendedor).mark_arc(
    innerRadius = 100,
    outerRadius = 150,
    
).encode(
    theta = alt.Theta(
        field = 'Valor Pedido', 
        type = 'quantitative',
        stack = True),

        color = alt.Color(
            field = 'Vendedor',
            type = 'nominal',
            legend = None
        ),
        
tooltip = ['Vendedor', 'Valor Pedido']

).properties(height = 500, width = 560, title = 'VALOR VENDA POR VENDEDOR')
rotulo_graf2_vendedor = graf2_Vendas_Vendedor.mark_text(radius = 210,size = 14).encode(text = 'Vendedor')
rotulo_graf2_Pedido   = graf2_Vendas_Vendedor.mark_text(radius = 180,size = 12).encode(text = 'Valor Pedido')

#Grafico Vendas por Cliente (Barras):
graf4_vendas_cliente = alt.Chart(tab4_Venda_Cliente).mark_bar(
    #color = cor_grafico,
    cornerRadiusTopLeft = 9,
    cornerRadiusTopRight = 9
).encode(
    x = 'Cliente',
    y = 'Valor Pedido',
    tooltip = ['Cliente', 'Valor Pedido']
).properties(height = altura_grafico, title = 'VENDAS POR CLIENTE').configure_axis(grid = False).configure_view(strokeWidth = 0)

#Gráfico de Vendas Mensais:

graf5_vendas_mensais = alt.Chart(tab5_Vendas_Mensais).mark_line(
    #color = cor_grafico,
).encode(
    alt.X('monthdate(Data):T'),
    y = 'Valor Pedido:Q'
).properties(height = altura_grafico, title = 'VENDAS MENSAIS').configure_axis(grid = False)#.configure_view(strokeWidth = 0)

# Página Principal:
#KPI's (Calculo):
total_vendas = round(tab2_vendas_margem['Valor Pedido'].sum(),2)
total_margem = round(tab2_vendas_margem['Margem Lucro'].sum(),2)
porc_margem = int(100 * (total_margem/total_vendas))

st.header(':bar_chart: DASHBOARD DE VENDAS') # ":bar_chart:" > icon 

dst1, dst2, dst3, dst4 = st.columns([1, 1, 1, 2.5]) # organizando os elementos (4 colunas)
with dst1:
    st.write('**VENDAS TOTAIS:**')
    st.info(f'R$ {total_vendas}')

with dst2:
    st.write('**MARGEM TOTAL:**')
    st.info(f'R$ {total_margem}')  

with dst3:
    st.write('**MARGEM %:**')
    st.info(f'{porc_margem} %') 
st.markdown("---")            

# Colunas dos Gráficos:

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.altair_chart(graf4_vendas_cliente, use_container_width = True)
    st.altair_chart(graf5_vendas_mensais, use_container_width = True)

with col2:
    st.altair_chart(graf1_qtd_produto, use_container_width = True)
    st.altair_chart(graf1_valor_produto, use_container_width = True)

with col3:     
    st.altair_chart(graf2_Vendas_Vendedor + rotulo_graf2_Pedido+ rotulo_graf2_vendedor)

st.markdown("---") 






  