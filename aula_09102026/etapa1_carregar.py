import pandas as pd

CAMINHO_CSV = "./aula_07102026/eleicoes.csv"


def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, dtype={"zona": str, "secao": str})
    return df


if __name__ == "__main__":
    df = carregar_dados()
    print(f"{len(df)} registros carregados")
    print(df.head(5))
