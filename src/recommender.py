from src.scripts.load_movies import load_movies
from src.scripts.genre_vectorizer import vectorize_genres
from src.scripts.similarity import compute_similarity

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


id_filme = 0  # Toy Story é geralmente o primeiro filme no ML-small
recs = recommend_by_index(id_filme, similarity_matrix, movies, n=20)
print(recs)
