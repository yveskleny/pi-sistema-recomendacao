from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(genre_matrix):
    """
    Recebe a matriz de gêneros (one-hot encoded) e calcula a similaridade
    entre os filmes usando a similaridade do cosseno.
    Retorna uma matriz de similaridade.
    """

    similarity_matrix = cosine_similarity(genre_matrix)
    return similarity_matrix
