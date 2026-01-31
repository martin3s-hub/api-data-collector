# API Data Collector

Projeto em Python que recolhe dados meteorológicos da API OpenWeather e guarda localmente em ficheiros JSON.

## Funcionalidades

- Consulta do tempo por cidade
- Suporte a múltiplas cidades
- Tratamento de erros de rede
- Guardar resultados com timestamp
- API key protegida via config.py

## Tecnologias

- Python 3
- Requests
- OpenWeather API
- Git + GitHub

## Como usar

1. Criar ficheiro `config.py`:

```python
API_KEY = "a_tua_api_key"
