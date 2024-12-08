from datetime import datetime 
from typing import Tuple

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutEnum(str, Enum):
    produto1 = "ZapFlow com ChatGPT"
    produto2 = "ZapFlow com Gemini"
    produto3 = "ZapFlow com Llama3.0"

class Vendas(BaseModel):
    """
    Essa é a classe de vendas do meu banco de dados

    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data de compra 
        valor (PositiveFloat): valor da compra 
        produto (Positiveint): nome do produto 
        quantidade (Positiveint): quantidade de produto
        produto (ProdutoEnum): Categoria do produto 
    """

    email: EmailStr
    date: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutEnum



