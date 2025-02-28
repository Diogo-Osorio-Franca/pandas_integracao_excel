import pandas as pd

#organizando as vendas de um mês digitado pelo usuário
df = pd.read_excel("planilha_teste_pandas.xlsx")

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

#soma as vendas de uma unidade durante o ano)
def vendas_total_loja():
    print("vendas totais da unidade")
    id_loja: int = int(input("digite o id da loja: "))
    print(df.loc[df['id_loja'] == id_loja].sum(axis=1,numeric_only=True))
    
vendas_total_loja()