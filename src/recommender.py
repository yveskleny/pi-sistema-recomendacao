from load_movies import load_movies
from genre_vectorizer import vectorize_genres
from similarity import compute_similarity

import numpy as np

# 1. Carregar os filmes
movies = load_movies()

# 2. Vetorizar os gêneros
genre_matrix, genres = vectorize_genres(movies)

# 3. Calcular similaridade
similarity_matrix = compute_similarity(genre_matrix)


def recommend_by_index(movie_index, matrix_sim, movies, n=10):
    """
    Retorna os n filmes mais similares dado um índice.
    """

    similaridades = matrix_sim[movie_index]
    indices_ordenados = np.argsort(similaridades)[::-1]

    # ignorar o próprio filme
    indices_ordenados = indices_ordenados[1 : n + 1]

    return movies.iloc[indices_ordenados]["title"]


def recommend_by_title(movie_title, matrix_sim, movies, n=10):
    """
    Retorna os n filmes mais similares dado um título.
    """

    movie_index = movies[movies["title"] == movie_title].index[0]
    return recommend_by_index(movie_index, matrix_sim, movies, n)

    # Exemplo de uso:


titulo_exemplo = "Terminator 3: Rise of the Machines (2003)"
recomendados = recommend_by_title(titulo_exemplo, similarity_matrix, movies, n=20)
print(f"Filmes recomendados para '{titulo_exemplo}':")
for filme in recomendados:
    print(f"- {filme}")
