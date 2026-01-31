# 🌦️ API Data Collector 🌤️

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-learning-success)

Projeto em Python que recolhe dados meteorológicos da API OpenWeather e guarda localmente os resultados em ficheiros JSON e CSV, um ficheiro JSON por cidade, por execução.

---

## 📌 Funcionalidades

- Consulta do tempo por cidade
- Suporte a múltiplas cidades
- Tratamento de erros de rede
- Guarda resultados com timestamp
- Cria automaticamente pasta `data/`

---

## 🛠️ Requisitos

- Python 3.10+
- Conta gratuita em https://openweathermap.org
- Biblioteca requests
---

## 🚀 Instalação

### 1. Clonar repositório

```
git clone https://github.com/martin3s-hub/api-data-collector.git
cd api-data-collector
```

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

Ativar (Windows):
```bash
.venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```
### 4. Configurar API Key

Cria um ficheiro `config.py` na raiz do projeto:
```python
API_KEY = "A_TUA_API_KEY_AQUI"
```
(Obtém a key em https://openweathermap.org
)

⚠️ Não faças commit do ficheiro `config.py` (já está incluído no `.gitignore`).

### 5. Executar o programa
```bash
python main.py
```
Introduz as cidades separadas por vírgulas:
```text
# exemplo de input
Lisboa, Porto, Madrid
```

Os ficheiros serão guardados automaticamente na pasta data/

Exemplo de output:

```json
{
    "cidade": "Lisboa",
    "temperatura": 18.4,
    "humidade": 72,
    "descricao": "céu limpo",
    "timestamp": "2026-01-31T10:32:12"
}
```

## 📈 Funcionalidades planeadas para evoluir o projeto:

- ~~Exportar dados para CSV~~ ✅
- Melhorar estrutura do projeto  
- Criar segundo projeto usando outra API  

---
## ⚙️ Como funciona

1. O utilizador introduz as cidades (separadas por vírgulas)
2. O programa consulta a API OpenWeather
3. Extrai os dados relevantes (temperatura, humidade, descrição, timestamp)
4. Guarda automaticamente:

   - um ficheiro JSON por cidade  
   - um ficheiro CSV acumulado  

O ficheiro CSV vai sendo atualizado a cada execução, criando um histórico simples dos dados recolhidos.

## 📁 Estrutura do projeto

```text
api-data-collector/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
└── data/
    ├── lisboa_2026-01-31_10-32-12.json
    ├── porto_2026-01-31_10-32-15.json
    └── dados.csv
```

---

## 🗺 Roadmap

- [x] Guardar dados em JSON  
- [x] Criar pasta automaticamente  
- [x] Timestamp nos ficheiros  
- [x] Exportar para CSV  
- [ ] Argumentos por linha de comando  
- [ ] Histórico diário  
- [ ] Gráficos simples  

---

## 🧠 Objetivo do projeto

Projeto criado para praticar:

- Python
- APIs REST
- JSON / CSV
- Automação simples
- Organização de projetos
- Requests



---
## 🧑‍💻 Autor

Pedro Martins  
Projeto criado para aprendizagem de Python, APIs e automação de dados.

