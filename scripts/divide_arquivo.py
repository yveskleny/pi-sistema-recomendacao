import pandas as pd

path = "/workspaces/pi-sistema-recomendacao/dados/TMDB_all_movies.csv"

movies_df = pd.read_csv(path)

quantidade_linhas = movies_df.shape[0]
numero_partes = 10

linhas_por_parte = quantidade_linhas // numero_partes

for i in range(numero_partes):
    inicio = i * linhas_por_parte
    if i == numero_partes - 1:
        fim = quantidade_linhas
    else:
        fim = (i + 1) * linhas_por_parte

    parte_df = movies_df.iloc[inicio:fim]
    parte_df.to_csv(f"/workspaces/pi-sistema-recomendacao/dados/TMDB_movies_part_{i + 1}.csv", index=False)
