import requests
import json
from datetime import datetime
from config import API_KEY

def obter_tempo(cidade):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q" : cidade,
        "appid" : API_KEY,
        "units" : "metric",
        "lang" : "pt"
    }

    try:
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()
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
    cidade_safe = info["cidade"].lower().replace(" ", "_")
    nome_ficheiro = f"data/{cidade_safe}_{timestamp}.json"
    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        json.dump(info, f, indent=4, ensure_ascii=False)

    print(f"Dados guardados em {nome_ficheiro}")

def main():
    entrada = input("Cidades (separadas por vírgulas): ")

    cidades = [c.strip() for c in entrada.split(",")]

    for cidade in cidades:
        print(f"\n A processar {cidade}...")

        dados = obter_tempo(cidade)

        if not dados:
            continue

        if dados.get("cod") != 200:
            print("Cidade não encontrada")
            continue

        info = extrair_info(dados)
        guardar_dados(info)


if __name__ == "__main__":
    main()

