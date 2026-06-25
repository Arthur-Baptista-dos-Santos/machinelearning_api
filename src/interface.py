import streamlit as st
import requests

st.set_page_config(page_title="Previsão de Imóveis", page_icon="🏠︎", layout="centered")
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
        "garagem": garagem
    }
    resposta = requests.post("http://127.0.0.1:8000/prever", json=payload)
    resultado = resposta.json()
    st.success(f"Preço estimado: **{resultado['preco_previsto']}**")
