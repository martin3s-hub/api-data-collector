import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="Gera gráfico de temperatura por cidade")
    parser.add_argument("cidade", help="Nome da cidade")

    args = parser.parse_args()
    cidade = args.cidade.lower()

    df = pd.read_csv("data/dados.csv")

    df["cidade"] = df["cidade"].str.lower()

    df_cidade = df[df["cidade"] == cidade]

    if df_cidade.empty:
        print("Cidade não encontrada no CSV.")
        return

    df_cidade = df_cidade.copy()
    df_cidade["timestamp"] = pd.to_datetime(df_cidade["timestamp"])

    df_cidade = df_cidade.sort_values("timestamp")

    os.makedirs("charts", exist_ok=True)

    plt.figure()
    plt.plot(df_cidade["timestamp"], df_cidade["temperatura"])
    plt.title(f"Temperatura em {cidade.title()}")
    plt.xlabel("Tempo")
    plt.ylabel("Temperatura (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    nome = f"charts/grafico_{cidade}.png"
    plt.savefig(nome)

    print(f"Gráfico guardado em {nome}")


if __name__ == "__main__":
    main()

