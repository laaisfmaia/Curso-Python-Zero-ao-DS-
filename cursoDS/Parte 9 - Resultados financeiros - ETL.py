import pandas as pd
from tabulate import tabulate
pd.set_option('display.float_format',lambda x: '%.3f' % x)

#load data
def get_data(path):
    df = pd.read_csv(path)
    return df


def tabela_compra(data):
    # agrupando os dados por região
    df = data[['zipcode', 'price']].groupby('zipcode').median().reset_index()
    df2 = pd.merge(data, df, on='zipcode', how='inner')

    # O imóvel vai ser sugerida para compra se:
    # - seu preço estiver abaixo da mediana da região;
    # - se a condição da casa estiver boa e
    # - se tiver vista para a água.
    for i in range(len(df2)):
        if (df2.loc[i, 'price_x'] < df2.loc[i, 'price_y']) & (df2.loc[i, 'condition'] >= 2) & (
                df2.loc[i, 'waterfront'] == 1):
            df2.loc[i, 'status'] = 'Compra'
        else:
            df2.loc[i, 'status'] = 'Não compra'

    #renomeando as colunas
    df2.rename(columns={'price_x': 'price', 'price_y': 'price_median'}, inplace=True)

    # dataframe com as sugestões de compra/não compra
    arq_sugestao_compra = df2[['id', 'zipcode', 'price', 'price_median', 'condition', 'waterfront', 'status']]

    # dataframe só com as casas que foram sugeridas para compra
    df3 = df2[df2['status'] == 'Compra'][['id', 'zipcode', 'price', 'price_median', 'condition', 'waterfront', 'status']]

    # salvando em um arquivo .csv
    arq_sugestao_compra.to_csv("sugestao_compra_imoveis.csv")

    # transformando em uma tabela para colocar no read.me
    tabela = tabulate(df3, tablefmt="pipe", headers="keys")

    return print(f'TABELA COM AS CASAS SUGERIDAS PARA A COMPRA:\n {tabela}')

def recomendacao_venda(data):
    #transformação da coluna 'date' para o tipo datetime
    data['date'] = pd.to_datetime(data['date'])

    # vou criar uma nova coluna chamada 'month' contendo somente o mês da coluna 'date'
    data['month'] = data['date'].dt.month

    # Verão: de junho a agosto.
    # Outono: de setembro a novembro.
    # Inverno: de dezembro a fevereiro.
    # Primavera: de março a maio.

    for i in range(len(data)):
        if data.loc[i, 'month'] in [6, 7, 8]:
            data.loc[i, 'season'] = 'summer'
        elif data.loc[i, 'month'] in [9, 10, 11]:
            data.loc[i, 'season'] = 'autumn'
        elif data.loc[i, 'month'] in [12, 1, 2]:
            data.loc[i, 'season'] = 'winter'
        else:
            data.loc[i, 'season'] = 'spring'

    # dataframe com a mediana do preço das casas para cada estação de cada zipcode
    df4 = data[['zipcode', 'season', 'price']].groupby(['zipcode', 'season']).median().reset_index()

    # salvando em um arquivo .csv
    df4.to_csv("zipcode-season.csv")

    #dataframe dos imóveis com os seus respectivos preços e a mediana
    df5 = pd.merge(data[['id', 'zipcode', 'season', 'price']], df4, on=['zipcode', 'season'], how='inner')

    #renomeando as colunas
    df5.rename(columns={'price_x': 'price', 'price_y': 'price_median'}, inplace=True)

    # Condições de venda:
    # 1. Se o preço da compra for maior que a mediana da região + sazonalidade:
    #    - O preço da venda será igual ao preço da compra + 10%
    # 2. Se o preço da compra for menor que a mediana da região + sazonalidade:
    #    - O preço da venda será igual ao preço da compra + 30

    for i in range(len(df5)):
        if (df5.loc[i, 'price'] > df5.loc[i, 'price_median']):
            df5.loc[i, 'price_sale'] = df5.loc[i, 'price'] + (df5.loc[i, 'price']) * (10 / 100)
            df5.loc[i, '%'] = '+10%'
        else:
            df5.loc[i, 'price_sale'] = df5.loc[i, 'price'] + (df5.loc[i, 'price']) * (30 / 100)
            df5.loc[i, '%'] = '+30%'
        #lucro
        df5.loc[i, 'lucro'] = df5.loc[i, 'price_sale'] - df5.loc[i, 'price']

    l_tot = df5['lucro'].sum()

    a = '\nSUGESTÃO DE PREÇO PARA VENDA: \n '
    b = '\nUtilizando essa metodologia no auxílio na tomada de decisão para definição do preço de compra e revenda dos imóveis proporcionará um lucro total de U$'

    return print(f'{a} {df5} {b}{l_tot:.2f}')

if __name__ == "__main__":
     # ETL - extração, transformação, carregamento
     # data extration
     path = 'datasets/kc_house_data.csv'

     # load data
     data = get_data(path)

     # tranformation data
     tabela_compra(data)
     recomendacao_venda(data)


