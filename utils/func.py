import pandas as pd
import os


# Função para carregar todos os arquivos CSV de um diretório
def carregar_csvs(diretorio):
    dataframes = {}
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.csv'):
            caminho = os.path.join(diretorio, arquivo)
            df_nome = arquivo.split('.')[0]
            # Carregando o DataFrame com o encoding 'utf-8-sig' para lidar com o BOM
            df = pd.read_csv(caminho, delimiter=';', encoding='utf-8-sig')
            # Limpeza adicional nos nomes das colunas para garantir a remoção de espaços extras e BOM (se por acaso não estiverem em UTF-8)
            df.columns = [col.strip().lstrip('\ufeff') for col in df.columns]
            dataframes[df_nome] = df
    return dataframes

# Função para comparar os campos comuns entre todos os DataFrames


def comparar_colunas(dataframes):
    listas_de_colunas = [set(df.columns.tolist())
                         for df in dataframes.values()]
    campos_comuns = set.intersection(*listas_de_colunas)
    return list(campos_comuns)

# Função para comparar as colunas diferentes entre dois DataFrames


def comparar_colunas_diferentes(df1, df2):
    colunas_df1 = set(df1.columns.tolist())
    colunas_df2 = set(df2.columns.tolist())

    exclusivas_df1 = list(colunas_df1 - colunas_df2)
    exclusivas_df2 = list(colunas_df2 - colunas_df1)

    return exclusivas_df1, exclusivas_df2


# Função para unir todos os DataFrames em um único DataFrame
def unir_dataframes(dataframes):
    # Encontrando os campos comuns entre todos os DataFrames
    campos_comuns = comparar_colunas(dataframes)

    # Filtrando cada DataFrame para manter apenas os campos comuns
    dfs_filtrados = [df[campos_comuns] for df in dataframes.values()]

    # Concatenando todos os DataFrames filtrados em um único DataFrame
    df_unido = pd.concat(dfs_filtrados, ignore_index=True)
    return df_unido

# Função para limpar os nomes das colunas de todos os DataFrames
def limpar_nomes(dataframes):
    for df in dataframes.values():
        df.columns = [col.strip().lstrip('\ufeff') for col in df.columns]
    return dataframes
