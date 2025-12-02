import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def load_movies():
    """
    Lê o arquivo movies.csv e retorna um DataFrame.
    Também faz a limpeza básica (como separar gêneros).
    """

    caminho = os.path.join(DATA_DIR, "movies.csv")
    filmes = pd.read_csv(caminho)

    # Criar um lista com os gêneros separados
    filmes["genres"] = filmes["genres"].apply(lambda x: x.split("|"))

    return filmes


def load_ratings():
    """
    Lê o arquivo ratings.csv contendo as notas dos usuários.
    Retorna DataFrame pronto para cálculos de popularidade.
    """

    caminho = os.path.join(DATA_DIR, "ratings.csv")
    notas = pd.read_csv(caminho)

    # Converter timestamp para datetime
    notas["timestamp"] = pd.to_datetime(notas["timestamp"], unit="s")

    return notas


def load_all_data():
    """
    Carrega todos os dados necessários (filmes e notas).
    Retorna dois DataFrames: filmes e notas.
    """

    filmes = load_movies()
    notas = load_ratings()

    return filmes, notas
