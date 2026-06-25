# `ML API (Previsão de Preço de Imóveis)`

> Modelo de machine learning servido como API REST com FastAPI e interface web com Streamlit.

---

## `Tecnologias`

![Python](https://img.shields.io/badge/Python-3.13-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![joblib](https://img.shields.io/badge/joblib-1.x-gray)

---

## `O que faz`

Treina um modelo de regressão linear sobre dados de imóveis, salva o modelo treinado em disco e o expõe via API REST. Uma interface Streamlit permite que qualquer usuário faça previsões de preço sem conhecimento técnico.

---

## `Pipeline`

```
imoveis.csv → treino (scikit-learn) → modelo.pkl
                                            ↓
                                      FastAPI /prever
                                            ↓
                                    interface Streamlit
```

---

## `Endpoints da API`

| `Método` | `Rota` | `Descrição` |
|---|---|---|
| GET | `/` | status da API |
| POST | `/prever` | recebe características do imóvel e retorna preço estimado |

**Exemplo de requisição:**

```json
POST /prever
{
  "area": 90.0,
  "quartos": 3,
  "banheiros": 2,
  "garagem": 1
}
```

**Resposta:**

```json
{
  "entrada": { "area": 90.0, "quartos": 3, "banheiros": 2, "garagem": 1 },
  "preco_previsto": "R$ 432.500"
}
```

---

## `Métricas do modelo`

| `Métrica` | `Valor` |
|---|---|
| R² (coeficiente de determinação) | ~0.97 |
| MAE (erro médio absoluto) | ~R$ 8.000 |

---

## `Pré-requisitos`

- Python 3.10+

---

## `Instalação`

```bash
git clone https://github.com/Arthur-Baptista-dos-Santos/ml-api.git
cd ml-api

python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
```

---

## `Uso`

```bash
# 1. Treinar o modelo e salvar em modelo/modelo.pkl
python src/treinar.py

# 2. Subir a API REST
uvicorn src.api:app --reload

# 3. (Terminal separado) Subir a interface web
streamlit run src/interface.py
```

A documentação interativa da API fica disponível em `http://127.0.0.1:8000/docs` (Swagger UI).

---

## `Estrutura`

```
ml-api/
├── dados/
│   └── imoveis.csv        # dataset de treinamento
├── modelo/
│   └── modelo.pkl         # modelo treinado (gerado localmente)
├── src/
│   ├── treinar.py         # treina e salva o modelo
│   ├── api.py             # API REST com FastAPI
│   └── interface.py       # interface web com Streamlit
├── .gitignore
├── requirements.txt
└── README.md
```

---

## `Conceitos aplicados`

- **`Regressão linear`**: prevê valor contínuo (preço) a partir de variáveis numéricas (área, quartos, banheiros, garagem)
- **`Train/test split`**: separa dados em treino (80%) e teste (20%) para avaliar generalização do modelo
- **`R²`**: mede quanto da variação do preço é explicada pelo modelo — 1.0 é perfeito
- **`MAE`**: erro médio absoluto em reais — quanto o modelo erra em média por imóvel
- **`joblib`**: serializa o modelo treinado em arquivo `.pkl` para uso sem retreinamento
- **`FastAPI`**: framework para construir APIs REST com validação automática via Pydantic
- **`Pydantic`**: valida e documenta os dados de entrada da API automaticamente
- **`Swagger UI`**: documentação interativa gerada automaticamente pelo FastAPI em `/docs`
