import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt


#lendo a planilha template
df = pd.read_excel("planilha_teste_pandas.xlsx")



#organizando as vendas de um mês digitado pelo usuário
def analise_ranking_vendas_mes():
    mes = input("digite o numéro do mês a ser organizado: ")
    analise = df.sort_values(by="vendas_" + mes,ascending=False)
    print(analise)


#somando as vendas realizadas em um mês digitado pelo usuário
def soma_mês():
    mes: int = int(input("digite o numéro do mês para que o total de vendas no período seja calculado: "))
    if mes >= 1 or mes <= 12:
        analise = df["vendas_"+str(mes)].sum()
        print(analise)


#retorna a loja que mais vendeu no mês pesquisado pelo usuário
def loja_top_mes():
    mes: int = int(input("digite o numéro do mês para descobrir a loja que mais performou durante o período: "))
    analise = df.sort_values(by="vendas_" + str(mes),ascending=False)
    print(analise.iloc[0,0])

#soma as vendas de uma unidade durante o ano
def vendas_total_loja():
    print("vendas totais da unidade")
    id_loja: int = int(input("digite o id da loja: "))
    #linha para somar a linha(axis=1) localizada com o valor digitado(df.loc[df['id_loja'] == id_loja])
    print(df.loc[df['id_loja'] == id_loja].sum(axis=1,numeric_only=True))

#retorna a media de vendas de uma unidade ao longo do ano
def media_ano_loja():
    print("média da unidade")
    id_loja: int = int(input("digite o id da loja: "))
    analise = df.loc[df['id_loja'] == id_loja].mean(axis=1,numeric_only=True)
    print(analise)

#retorna a media de vendas em um mês informado
def media_vendas_mes():
    mes: int = int(input("digite o numéro do mês que deseja saber a media de vendas: "))
    analise = df["vendas_"+str(mes)].mean(axis=0,numeric_only=True)
    print(analise)
#retorna um gráfico em matplotlib mostrando o faturamento no eixo y e o id das lojas no eixo X
def graficos_vendas_mes():
    mes: int = int(input("digite o numéro do mês para obter o gráfico correspondente: "))
    grafico = df["vendas_" + str(mes)].plot(kind="bar")
    grafico.set(xlabel="Id da loja", ylabel="faturamento",title="Vendas por loja")
    lista = df.index.tolist()
    lista_numpy = numpy.array(lista)
    lista_numpy = lista_numpy + 1
    grafico.set_xticklabels(lista_numpy)
    plt.xticks(range(1,30))
    plt.show()

