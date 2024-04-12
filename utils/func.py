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

# Função para limpar os nomes das colunas de todos os DataFrames


def limpar_nomes(dataframes):
    for df in dataframes.values():
        df.columns = [col.strip().lstrip('\ufeff') for col in df.columns]
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

# Função para salvar um DataFrame em um arquivo CSV


def salvar_dataframe_em_csv(df, caminho_saida, nome_arquivo, index=False, sep=';', **kwargs):
    """
    Salva um DataFrame em um arquivo CSV.

    Parâmetros:
    - df: DataFrame a ser salvo.
    - caminho_saida: String do caminho do diretório onde o arquivo será salvo.
    - nome_arquivo: Nome do arquivo CSV (incluindo a extensão .csv).
    - index: Booleano indicando se o índice do DataFrame deve ser salvo no arquivo.
    - sep: Caractere usado como separador de colunas no arquivo.
    - **kwargs: Argumentos adicionais suportados por pandas.DataFrame.to_csv().
    """

    # Verifica se o diretório de saída existe. Se não, cria o diretório.
    if not os.path.exists(caminho_saida):
        os.makedirs(caminho_saida)

    # Monta o caminho completo onde o arquivo será salvo
    caminho_completo = os.path.join(caminho_saida, nome_arquivo)

    # Salva o DataFrame no caminho especificado
    df.to_csv(caminho_completo, index=index, sep=sep, **kwargs)
    print(f"Arquivo salvo com sucesso em: {caminho_completo}")
