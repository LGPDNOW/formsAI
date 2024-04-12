from utils.func import carregar_csvs, comparar_colunas, comparar_colunas_diferentes

diretorio_base = 'base/'
dataframes = carregar_csvs(diretorio_base)

campos_comuns = comparar_colunas(dataframes)
print("Campos comuns a todos os DataFrames:", campos_comuns)


# Escolhendo dois DataFrames específicos para comparar
df1_nome, df2_nome = 'nome_df1', 'nome_df2'  # Substitua pelos nomes reais dos seus DataFrames
df1, df2 = dataframes[df1_nome], dataframes[df2_nome]

exclusivas_df1, exclusivas_df2 = comparar_colunas_diferentes(df1, df2)
print(f"Colunas exclusivas ao {df1_nome}: {exclusivas_df1}")
print(f"Colunas exclusivas ao {df2_nome}: {exclusivas_df2}")
