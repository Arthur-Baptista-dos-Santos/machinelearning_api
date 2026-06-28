import streamlit as st
import numpy as np
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "modelo" / "modelo.pkl"
modelo = joblib.load(MODEL_PATH)

st.set_page_config(page_title="Previsao de Imoveis", layout="centered")
st.title("Previsao de Preco de Imoveis")
st.markdown("Preencha as caracteristicas do imovel para obter uma estimativa de preco.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (m2)", min_value=10.0, max_value=500.0, value=90.0)
    quartos = st.slider("Quartos", 1, 10, 3)

with col2:
    banheiros = st.slider("Banheiros", 1, 10, 2)
    garagem = st.slider("Vagas de garagem", 0, 5, 1)

st.divider()

if st.button("Calcular preco", type="primary"):
    dados = np.array([[area, quartos, banheiros, garagem]])
    preco = modelo.predict(dados)[0]
    st.success(f"Preco estimado: R$ {preco:,.0f}")

    with st.expander("Detalhes da estimativa"):
        st.json({
            "area_m2": area,
            "quartos": quartos,
            "banheiros": banheiros,
            "garagem": garagem,
            "preco_previsto": f"R$ {preco:,.0f}",
            "modelo": "Regressao Linear"
        })
