from fastapi import FastAPI
from typing import List

from app.schema import ProdutosSchema
from app.data import Produtos

app = FastAPI()
lista_de_produtos = Produtos()

@app.get("/")    # Request
def ola_mundo(): # Response
    return {"Olá": "Mundo!"}

@app.get("/produtos", response_model=List[ProdutosSchema])
def listar_produtos():
    return lista_de_produtos.listar_produtos()

@app.get("/produtos/{id}", response_model=ProdutosSchema)
def listar_produto(id: int):
    return lista_de_produtos.listar_produto(id)

@app.post("/produtos/{id}", response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema):
    return lista_de_produtos.adicionar_produto(produto.model_dump())