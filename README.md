# 🌦️ API Data Collector

Projeto em Python que recolhe dados meteorológicos da API OpenWeather e guarda localmente os resultados em ficheiros JSON, um ficheiro por cidade e execução.

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

Ativar:
```md
Windows

.venv\Scripts\activate
```

### 3. Instalar dependências
```terminal
pip install -r requirements.txt
```
### 4. Configurar API Key

Cria um ficheiro `config.py` na raiz do projeto:
```python
API_KEY = "A_TUA_API_KEY_AQUI"
```
(Obtém a key em https://openweathermap.org
)

### 5. Executar o programa
```terminal
python main.py
```
Introduz as cidades separadas por vírgulas:
```terminal
Lisboa, Porto, Madrid
```

Os ficheiros serão guardados automaticamente na pasta data/

## 📈 Próximos passos

- Exportar dados para CSV  
- Melhorar estrutura do projeto  
- Criar segundo projeto usando outra API  

## 🧑‍💻 Autor

Pedro Martins  
Projeto criado para aprendizagem de Python, APIs e automação de dados.