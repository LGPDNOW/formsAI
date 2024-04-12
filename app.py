from utils.func import *  # Importa todas as funções do arquivo utils/func.py

diretorio_base = 'base/'
dataframes = carregar_csvs(diretorio_base)

campos_comuns = comparar_colunas(dataframes)
print("Campos comuns a todos os DataFrames:", campos_comuns)


# Escolhendo dois DataFrames específicos para comparar
# Substitua pelos nomes reais dos seus DataFrames
df1_nome, df2_nome = 'flamengo', 'oab_sp'
df1, df2 = dataframes[df1_nome], dataframes[df2_nome]

exclusivas_df1, exclusivas_df2 = comparar_colunas_diferentes(df1, df2)
print(f"Colunas exclusivas ao {df1_nome}: {exclusivas_df1}")
print(f"Colunas exclusivas ao {df2_nome}: {exclusivas_df2}")


df_unido = unir_dataframes(dataframes)
print(df_unido.columns.tolist())
len(df_unido.columns.tolist())


diretorio_saida = 'out/'
nome_arquivo = 'dados_unidos.csv'

# Salvando o DataFrame em um arquivo CSV
salvar_dataframe_em_csv(df_unido, diretorio_saida, nome_arquivo, index=False)
