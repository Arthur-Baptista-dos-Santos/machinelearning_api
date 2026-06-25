from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np

app = FastAPI(title="API de Previsão de Imóveis")

modelo = joblib.load("modelo/modelo.pkl")

class Imovel(BaseModel):
    area: float = Field(..., gt=0, example=90.0, description="Área do imóvel em metros quadrados") # type: ignore
    quartos: int = Field(..., ge=1, le=10, example=3, description="Número de quartos") # type: ignore
    banheiros: int = Field(..., ge=1, le=10, example=2, description="Número de banheiros") # type: ignore
    garagem: int = Field(..., ge=0, le=5, example=1, description="Vagas de garagem (0 = sem garagem)") # type: ignore

@app.get("/")
def root():
    return {"status": "online", "modelo": "regressão linear — previsão de preço de imóveis"}

@app.post("/prever")
def prever(imovel: Imovel):
    dados = np.array([[imovel.area, imovel.quartos, imovel.banheiros, imovel.garagem]])
    preco = modelo.predict(dados)[0]
    return {
        "entrada": imovel.model_dump(),
        "preco_previsto": f"R$ {preco:,.0f}"
    }
