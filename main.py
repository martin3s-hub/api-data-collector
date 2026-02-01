import requests
import json
import csv
import argparse
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY não encontrada. Verifica o ficheiro .env")

def obter_tempo(cidade):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt"
    }

    try:
        resposta = requests.get(url, params=params, timeout=10)

        if resposta.status_code == 404:
            return {"erro": "cidade"}

        if resposta.status_code != 200:
            return {
                "erro": "api",
                "codigo": resposta.status_code,
                "mensagem": resposta.reason
            }

        return resposta.json()

    except requests.exceptions.RequestException as e:
        print(f"Erro de rede para {cidade}: {e}")
        return None


def extrair_info(dados):
    info = {
        "cidade": dados["name"],
        "temperatura": dados["main"]["temp"],
        "humidade": dados["main"]["humidity"],
        "descricao": dados["weather"][0]["description"],
        "timestamp": datetime.now().isoformat()
        }

    return info

def guardar_dados(info):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    cidade_safe = info["cidade"].lower().replace(" ", "-")
    nome_ficheiro = f"data/{cidade_safe}_{timestamp}.json"
    os.makedirs("data", exist_ok=True)
    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4, ensure_ascii=False)

    print(f"Dados guardados em {nome_ficheiro}")

def guardar_csv(info):
    os.makedirs("data", exist_ok=True)
    ficheiro_csv = "data/dados.csv"
    ficheiro_existe = os.path.isfile(ficheiro_csv)

    with open(ficheiro_csv, "a", newline="", encoding="utf-8") as csvfile:
        campos = info.keys()
        writer = csv.DictWriter(csvfile, fieldnames=campos)

        if not ficheiro_existe:
            writer.writeheader()

        writer.writerow(info)

    print("Dados adicionados ao CSV")


def main():
    parser = argparse.ArgumentParser(description="Recolhe dados meteorológicos por cidade")

    parser.add_argument(
        "--csv-only",
        action="store_true",
        help="Guarda apenas no CSV (não cria ficheiros JSON)"
    )

    parser.add_argument(
        "cidades",
        nargs="*",
        help="Lista de cidades (ex: Lisboa Porto Madrid)"
    )

    args = parser.parse_args()

    if args.cidades:
        cidades = args.cidades

    else:
        entrada = input("Cidades (separadas por vírgulas): ")
        cidades = [c.strip() for c in entrada.split(",")]

    for cidade in cidades:
        print(f"\n A processar {cidade}...")

        dados = obter_tempo(cidade)

        if not dados:
            continue

        if dados.get("erro") == "cidade":
            print("Cidade não encontrada")
            continue

        if dados.get("erro") == "api":
            print(f"Erro da API ({dados['codigo']}): {dados['mensagem']}")
            continue

        info = extrair_info(dados)
        if not args.csv_only:
            guardar_dados(info)

        guardar_csv(info)


if __name__ == "__main__":
    main()

