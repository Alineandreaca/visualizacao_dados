# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import altair as alt
from waitress import serve
from teste2 import app  # Substitua 'your_app' pelo nome do seu módulo

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)


app = Dash(__name__)
#server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


#base de dados que gera o gráfico  para matemática (apenas para os totais)
df_pisa_math = pd.read_csv("pisa1.csv")
df_pisa_math_filtrada = df_pisa_math.loc[df_pisa_math['SUBJECT']=='TOT']
#---------------criando o gráfico------------------------------------------------------------------------------
fig= px.bar(df_pisa_math_filtrada, x="LOCATION", y="Value", labels=dict(x='País', y='Pontuação'),color= None,barmode="group",  title='Gráfico de Barras das pontuações médias - Matemática')
opcoes = list(df_pisa_math_filtrada['TIME'].unique())
opcoes.append("Todos os anos")
#---------------base de dados que gera o gráfico  para ciência (apenas para os totais)-------------------------
df_pisa_sci = pd.read_csv("pisa2.csv")
df_pisa_sci_filtrada = df_pisa_sci.loc[df_pisa_sci['SUBJECT']=='TOT']
#---------------criando o gráfico------------------------------------------------------------------------------
fig2= px.bar(df_pisa_sci_filtrada, x="LOCATION", y="Value", labels=dict(x='País', y='Pontuação'),color=None, barmode="group", title='Gráfico de Barras das pontuações médias - Ciências')
opcoes = list(df_pisa_sci_filtrada['TIME'].unique())
opcoes.append("Todos os anos")
#---------------base de dados que gera o gráfico  para leitura(apenas para os totais)-------------------------
df_pisa_read = pd.read_csv("pisa3.csv")
df_pisa_read_filtrada = df_pisa_read.loc[df_pisa_read['SUBJECT']=='TOT']
#---------------Gráfico de Barras------------------------------------------------------------------------------
fig3= px.bar(df_pisa_read_filtrada, x="LOCATION", y="Value", labels=dict(x='País', y='Pontuação'), color=None, barmode="group", title='Gráfico de Barras das pontuações médias - Leitura')
opcoes = list(df_pisa_sci_filtrada['TIME'].unique())
opcoes.append("Todos os anos")
#----------------Gráfico de Dispersão--------------------------------------------------------------------------
fig4= px.scatter(data_frame=df_pisa_math, x='Value', y= 'LOCATION', color='SUBJECT', hover_name='TIME', height=800, color_discrete_sequence= ['#00bfff', '#c71585', '#ff7f50'], title='Gráfico de dispersão - Matemática')
fig5= px.scatter(data_frame=df_pisa_sci, x='Value', y= 'LOCATION', color='SUBJECT', hover_name='TIME', height=800, color_discrete_sequence= ['#00bfff', '#c71585', '#ff7f50'],  title='Gráfico de dispersão - Ciência')
fig6= px.scatter(data_frame=df_pisa_read, x='Value', y= 'LOCATION', color='SUBJECT', hover_name='TIME', height=800, color_discrete_sequence= ['#00bfff', '#c71585', '#ff7f50'], title='Gráfico de dispersão - Leitura')

#---------Boxplot------------------------------------------------------------------------------
fig7= px.box(data_frame=df_pisa_math, x='TIME', y= 'Value', color='SUBJECT', hover_name='LOCATION', color_discrete_sequence= ['#00bfff', '#c71585', '#ff7f50'], title='Boxplot- Matemática' )
fig8= px.box(data_frame=df_pisa_sci, x='TIME', y= 'Value', color='SUBJECT', hover_name='LOCATION' , color_discrete_sequence= ['#00bfff', '#c71585', '#ff7f50'], title='Boxplot- Ciência' )
fig9= px.box(data_frame=df_pisa_read, x='TIME', y= 'Value', color='SUBJECT', hover_name='LOCATION', color_discrete_sequence= ['#00bfff', '#c71585', '#ff7f50'], title='Boxplot- Leitura' )

#--------Mapa de calor------------------------------------------------------------------------------
fig10= px.density_heatmap(data_frame= df_pisa_math, x='LOCATION', y= 'TIME', z='Value', histfunc='avg', height=800, title='Mapa de Calor de Matemática')
fig11= px.density_heatmap(data_frame= df_pisa_sci, x='LOCATION', y= 'TIME', z='Value', histfunc='avg', height=800, title='Mapa de Calor de Ciência')
fig12= px.density_heatmap(data_frame= df_pisa_read, x='LOCATION', y= 'TIME', z='Value', histfunc='avg', height=800, title='Mapa de Calor de Leitura')
#---------Histograma------------------------------------------------------------------------------
fig13= px.histogram(data_frame=df_pisa_math, x='Value', color='SUBJECT', title='Histograma das pontuações médias - Matemática', 
                    color_discrete_sequence= ['#00bfff', '#c71585', '#ff7f50']) 

fig14= px.histogram(data_frame=df_pisa_sci, x='Value', color='SUBJECT', title='Histograma das pontuações médias - Ciência', 
                    color_discrete_sequence= ['#00bfff', '#c71585', '#ff7f50']) 

fig15= px.histogram(data_frame=df_pisa_read, x='Value', color='SUBJECT', title='Histograma das pontuações médias - Leitura', 
                    color_discrete_sequence= ['#00bfff', '#c71585', '#ff7f50']) 


# Personaliza os eixos X e Y
# Define layout do Heatmap - ok
fig10.update_layout(
    xaxis=dict(title='País'),
    yaxis=dict(title='Ano')
    ) 
fig11.update_layout(
    xaxis=dict(title='País'),
    yaxis=dict(title='Ano')
    ) 
fig12.update_layout(
    xaxis=dict(title='País'),
    yaxis=dict(title='Ano')
    ) 

# Define layout do Dispersão  - ok
fig4.update_layout(
    xaxis=dict(title='Pontuação'),
    yaxis=dict(title='País')
    ) 
fig5.update_layout(
    xaxis=dict(title='Pontuação'),
    yaxis=dict(title='País')
    ) 
fig6.update_layout(
    xaxis=dict(title='Pontuação'),
    yaxis=dict(title='País')
    ) 

# Define layout do Boxplot - ok
fig7.update_layout(
    xaxis=dict(title='Ano'),
    yaxis=dict(title='Pontuação')
    ) 
fig8.update_layout(
    xaxis=dict(title='Ano'),
    yaxis=dict(title='Pontuação')
    ) 
fig9.update_layout(
    xaxis=dict(title='Ano'),
    yaxis=dict(title='Pontuação')
    ) 

# Define layout do Histograma - ok
fig13.update_layout(
    xaxis=dict(title='Pontuação'),
    yaxis=dict(title='Contagem')
    ) 
fig14.update_layout(
    xaxis=dict(title='Pontuação'),
    yaxis=dict(title='Contagem')
    ) 
fig15.update_layout(
    xaxis=dict(title='Pontuação'),
    yaxis=dict(title='Contagem')
    ) 
#fimdoteste


app.layout = html.Div(
    children=[
        html.H1(className="title", children='ANÁLISE DOS RESULTADOS DO PROGRAMA INTERNACIONAL DE AVALIAÇÃO DE ESTUDANTES (Pisa)'),
            html.Div(className="container", children=[
                html.P('''
                O Programa Internacional de Avaliação de Estudantes (Pisa), tradução de Programme for International Student Assessment,é um estudo comparativo internacional realizado a cada três anos pela Organização para a Cooperação e Desenvolvimento Econômico (OCDE), que
                oferece insights incomparáveis sobre a qualidade da educação em leitura, matemática e ciências em todo o mundo.'''),
                html.P('''Com o PISA, você pode entender o que diferencia os sistemas educacionais de alto desempenho 
                dos demais e aprender as estratégias que levaram ao sucesso.'''),
                html.P('''Oferecendo informações sobre o desempenho dos estudantes na faixa etária dos 15 anos, idade em que se pressupõe o término da 
                escolaridade básica obrigatória na maioria dos países, vinculando dados sobre suas atitudes em relação à aprendizagem, e também aos
                principais fatores que moldam sua aprendizagem, dentro e fora da escola.'''),
                html.P('''Nesta análise abrangente, exploramos as tendências que surgiram ao longo dos anos, os desafios enfrentados e as vitórias alcançadas. Cada gráfico conta uma história poderosa 
                sobre o progresso educacional global e oferece lições valiosas para o futuro.    
            '''),
    ]),     
        html.H2(children='Gráficos de Barras', className="texto"),
            #html.Div(id='texto'),
            html.Div(className="container", children=[  
                html.P('''O gráfico de barras a seguir apresenta a  distribuição das soma das pontuações médias obtidas pelos alunos em uma 
                avaliação escolar recente. Este tipo de gráfico é uma ferramenta visual eficaz para comparar os resultados de diferentes
                grupos ou categorias. Elementos do gráfico de barras: '''),
                html.P('''Barras: Cada barra representa a soma das média das pontuações dos países. '''),   
                html.P('''Eixo Horizontal (X): Representa os diferentes países.'''),
                html.P('''Eixo Vertical (Y): Representa as pontuações médias. '''),
                html.P('''Este gráfico de barras ajuda a identificar: '''),
                html.P('''Comparação entre Grupos: Facilita a comparação das pontuações médias entre diferentes grupos de alunos ou categorias, destacando aqueles que estão se saindo melhor ou pior.
                '''),
                html.P(''' Desempenho Geral: Proporciona uma visão clara do desempenho médio em toda a avaliação, permitindo identificar áreas fortes e fracas.
                '''),
                html.P('''Tendências: Permite observar tendências gerais, como se certos temas estão consistentemente acima ou abaixo da média.O gráfico de barras a seguir apresenta a  distribuição das soma das pontuações médias obtidas pelos alunos em uma avaliação escolar recente. 
                '''),
            ]),
            dcc.Dropdown(opcoes, 'Todos os anos', id='dropdown', className="dropdownconfig"),
            dcc.Graph(
            className="grafico",
            id='example-graph',
            figure=fig
    ),
        html.H2(className="title"),
            dcc.Graph(
            className="grafico",
            id='example-graph2',
            figure=fig2
    ),
    
        html.H2(className="title"),
            dcc.Graph(
            className="grafico",
            id='example-graph3',
            figure=fig3
    ),
        html.H2(children='Mapas de Calor', className="texto"),
        html.Div(className="container", children=[  
                html.P('''O heatmap a seguir apresenta a distribuição das pontuações obtidas pelos alunos em uma avaliação escolar recente. 
                Este gráfico de calor é uma ferramenta visual que utiliza cores para representar os valores das pontuações, facilitando a identificação de padrões e tendências nos dados.
                Elementos do heatmap:'''),
                html.P('''Cores: Cada célula do heatmap é colorida de acordo com a intensidade das pontuações médias dos países durante os anos, 
                com cores mais escuras ou vibrantes indicando valores mais altos e cores mais claras indicando valores mais baixos. '''),
                html.P('''Eixos: O eixo horizontal representa os anos de aplicação da avaliação, enquanto o eixo vertical representa os país.'''),
                html.P('''Legenda: Uma escala de cores ao lado do heatmap ajuda a interpretar os valores médios correspondentes às cores exibidas.'''),
            ]),
        
            dcc.Graph(
            className="grafico",
            id='example-graph10',
            figure=fig10
    ),
            html.H2(className="title"),
            dcc.Graph(
            className="grafico",
            id='example-graph11',
            figure=fig11
    ),
            html.H2(className="title"),
            dcc.Graph(
            className="grafico",
            id='example-graph12',
            figure=fig12
    ),
        html.H2(children='Gráficos de Dispersão', className='texto'),
            html.Div(className="container", children=[  
                html.P('''O gráfico de dispersão a seguir apresenta a relação entre as pontuações obtidas pelos alunos em avaliações no intervalo de anos. 
                Este tipo de gráfico, também conhecido como scatter plot, é uma ferramenta visual que ajuda a identificar correlações e padrões entre duas 
                variáveis. Elementos do gráfico de dispersão:'''),
                html.P('''Pontos: Cada ponto no gráfico representa um aluno, com suas coordenadas (x, y) indicando suas pontuações nas avaliações. '''),
                html.P('''Eixos: O eixo horizontal (x) representa as pontuações nas avaliações, enquanto o eixo vertical (y) representa os países.
                '''),
                html.P('''Linha de Tendência (opcional): Uma linha de tendência pode ser adicionada para visualizar a correlação entre as pontuações das avaliações.'''),
            ]),
               
            dcc.Graph(
            className="grafico",
            id='example-graph4',
            figure=fig4
    ), 
        html.H2(className="title"),
            dcc.Graph(
            className="grafico",
            id='example-graph5',
            figure=fig5
    ),
        html.H2(className="title"),
            dcc.Graph(
            className="grafico",
            id='example-graph6',
            figure=fig6
    ),
        html.H2(children='Boxplots', className='texto'),
            html.Div(className="container", children=[
                html.P('''
                O boxplot a seguir apresenta uma visão estatística detalhada das pontuações obtidas pelos alunos ao longo dos anos. 
                Este gráfico, também conhecido como diagrama de caixa, é uma ferramenta estatística que resume a distribuição das 
                pontuações e destaca as principais características dos dados. Elementos do boxplot: '''),
                html.P('''Caixa (Box): Representa o intervalo interquartil (IQR), que contém os 50% das pontuações centrais. A linha dentro da caixa indica a mediana, que é o valor central das pontuações.
                '''),
                html.P('''Extensões (Whiskers): Estendem-se das extremidades da caixa até o menor e maior valor dentro de 1,5 vezes o IQR a partir dos quartis inferiores e superiores, respectivamente.
                '''),
                html.P('''Pontos Fora da Caixa: Valores fora deste intervalo são considerados outliers e são representados por pontos individuais.   '''),
            ]),  
            html.Div(className="container", children=[  
                html.P('''Este boxplot nos ajuda a identificar:  '''),
                html.P('''Dispersão das Pontuações: A largura da caixa e a extensão dos whiskers mostram a variabilidade das pontuações. '''),
                html.P('''Tendência Central: A posição da mediana dentro da caixa indica se os dados são simétricos ou se há um viés.  '''),
                html.P('''Outliers: Pontuações que são significativamente diferentes das demais, indicando possíveis anomalias ou áreas que necessitam de atenção especial. '''),
            ]),
        
            dcc.Graph(
            className="grafico",
            id='example-graph7',
            figure=fig7
    ),
        html.H2(className="title"),
            dcc.Graph(
            className="grafico",
            id='example-graph8',
            figure=fig8
    ),
        html.H2(className="title"),
            dcc.Graph(
            className="grafico",
            id='example-graph9',
            figure=fig9
    ),
        html.H2(children='Histogramas', className="texto"),
            html.Div(className="container", children=[
                html.P('''
                O histograma a seguir apresenta a distribuição das pontuações médias obtidas pelos alunos nas avaliações do Pisa. '''),
                html.P('''Cada barra do histograma representa a frequência de alunos cujas pontuações médias caem dentro de intervalos específicos.'''),
                html.P('''Podemos identificar facilmente quais intervalos de pontuação são mais comuns e observar a dispersão dos resultados.'''),
            ]),
            dcc.Graph(
            className="grafico",
            id='example-graph13',
            figure=fig13
    ),
        html.H2(className="title"),
            dcc.Graph(
            className="grafico",
            id='example-graph14',
            figure=fig14
    ),
        html.H2(className="title"),
            dcc.Graph(
            className="grafico",
            id='example-graph15',
            figure=fig15
    )
])
#callback matemática
@app.callback(
    Output('example-graph', 'figure'),
    Input('dropdown', 'value')
)
def update_output(value):
    if value == "Todos os anos":
        fig = px.bar(df_pisa_math_filtrada, x="LOCATION", y="Value", labels=dict(x='País', y='Pontuação'),color=None, barmode="group", title='Gráfico de Barras das pontuações médias - Matemática', color_discrete_sequence=['#00008B'])
        fig.update_layout(
            xaxis=dict(title='País'),
            yaxis=dict(title='Pontuação')
            ) 
    else:
        tabela_filtrada = df_pisa_math_filtrada.loc[df_pisa_math_filtrada['TIME']==value,:] 
        fig = px.bar(tabela_filtrada, x="LOCATION", y="Value", labels=dict(x='País', y='Pontuação'),color=None, barmode="group", title='Gráfico de Barras das pontuações médias - Matemática', color_discrete_sequence=['#00008B'])
        fig.update_layout(
            xaxis=dict(title='País'),
            yaxis=dict(title='Pontuação')
            ) 
    return fig

#callback ciência
@app.callback(
    Output('example-graph2', 'figure'),
    Input('dropdown', 'value')
)

def update_output(value):
    if value == "Todos os anos":
        fig = px.bar(df_pisa_sci_filtrada, x="LOCATION", y="Value", labels=dict(x='País', y='Pontuação'),color=None, barmode="group", title='Gráfico de Barras das pontuações médias - Ciências', color_discrete_sequence=['#006400'])
        fig.update_layout(
            xaxis=dict(title='País'),
            yaxis=dict(title='Pontuação')
            )     
    else:
        tabela_filtrada_sci = df_pisa_sci_filtrada.loc[df_pisa_sci_filtrada['TIME']==value,:] 
        fig = px.bar(tabela_filtrada_sci, x="LOCATION", y="Value", labels=dict(x='País', y='Pontuação'),color=None, barmode="group", title='Gráfico de Barras das pontuações médias - Ciências', color_discrete_sequence=['#006400'])
        fig.update_layout(
            xaxis=dict(title='País'),
            yaxis=dict(title='Pontuação')
            ) 
    return fig

#callback leitura

@app.callback(
    Output('example-graph3', 'figure'),
    Input('dropdown', 'value')
)

def update_output(value):
    if value == "Todos os anos":
        fig = px.bar(df_pisa_read_filtrada, x="LOCATION", y="Value",color=None, barmode="group", title='Gráfico de Barras das pontuações médias - Leitura', color_discrete_sequence=['#FF6347'])
        fig.update_layout(
            xaxis=dict(title='País'),
            yaxis=dict(title='Pontuação')
            ) 
    else:
        tabela_filtrada_read = df_pisa_read_filtrada.loc[df_pisa_read_filtrada['TIME']==value,:] 
        fig = px.bar(tabela_filtrada_read, x="LOCATION", y="Value", labels=dict(x='País', y='Pontuação'),color=None, barmode="group",  title='Gráfico de Barras das pontuações médias - Leitura', color_discrete_sequence=['#FF6347'])
        fig.update_layout(
            xaxis=dict(title='País'),
            yaxis=dict(title='Pontuação')
            ) 
    return fig

if __name__ == '__main__':
    app.run(debug=True)
