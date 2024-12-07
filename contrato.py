from datetime import datetime 
from typing import Tuple

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutEnum(str, Enum):
    produto1 = "ZapFlow com ChatGPT"
    produto2 = "ZapFlow com Gemini"
    produto3 = "ZapFlow com Llama3.0"

class Vendas(BaseModel):
    email: EmailStr
    date: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutEnum



