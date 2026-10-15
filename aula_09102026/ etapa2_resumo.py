from rich.panel import Panel
from etapa1_carregar import carregar_dados
from formatacao import console, numero_br


def mostrar_resumo(df):
    total_registros = len(df)  # quantidade de linhas
    total_votos = df["votos"].sum()  # soma da coluna votos
    total_cidades = df["cidade"].nunique()  # quantas cidades diferentes
    total_candidatos = df["candidato"].nunique()  # quantos candidatos diferentes

    texto = (
        f"[bold]Registros:[/] {numero_br(total_registros)} "
        f"[bold]Votos:[/] {numero_br(total_votos)} "
        f"[bold]Cidades:[/] {total_cidades} "
        f"[bold]Candidatos:[/] {total_candidatos}"
    )

    console.print(Panel(texto, title="Eleições 2024 (dados fictícios)", expand=False))

if __name__ == "__main__":
    df = carregar_dados()
    mostrar_resumo(df)
