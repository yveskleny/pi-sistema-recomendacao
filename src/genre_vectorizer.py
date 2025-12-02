from sklearn.preprocessing import MultiLabelBinarizer


def vectorize_genres(movies_df):
    """
    Recebe o DataFrame de filmes com a coluna 'genres' (lista de strings)
    e devolve a matriz de gêneros em formato one-hot encoded.
    """

    mlb = MultiLabelBinarizer()

    genre_matrix = mlb.fit_transform(movies_df["genres"])
    return genre_matrix, mlb.classes_
