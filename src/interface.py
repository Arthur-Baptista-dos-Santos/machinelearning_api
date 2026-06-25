import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/prever"

st.set_page_config(page_title="Previsão de Imóveis", layout="centered")
st.title("Previsão de Preço de Imóveis")
st.markdown("Preencha as características do imóvel para obter uma estimativa de preço.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Área (m²)", min_value=10.0, max_value=500.0, value=90.0)
    quartos = st.slider("Quartos", 1, 10, 3)

with col2:
    banheiros = st.slider("Banheiros", 1, 10, 2)
    garagem = st.slider("Vagas de garagem", 0, 5, 1)

st.divider()

if st.button("Calcular preço", type="primary"):
    payload = {
        "area": area,
        "quartos": quartos,
        "banheiros": banheiros,
        "garagem": garagem,
    }
    try:
        resposta = requests.post(API_URL, json=payload, timeout=5)
        resposta.raise_for_status()
        resultado = resposta.json()
        st.success(f"Preço estimado: **{resultado['preco_previsto']}**")
    except requests.exceptions.ConnectionError:
        st.error("API offline. Inicie a API com: `uvicorn src.api:app --reload`")
    except requests.exceptions.HTTPError as e:
        st.error(f"Erro na API: {e}")
    except Exception as e:
        st.error(f"Erro inesperado: {e}")
