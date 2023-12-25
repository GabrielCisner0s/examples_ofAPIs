from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None #por defecto, si no se envia el valor id, que tenga un valor None
    name: str = Field(default="New Product", min_length=5, max_length=15)#Default daria un nombre por defecto en caso de que las condiciones de limite de caracteres no se cumpla
    price: float = Field(default=0, ge=0, le=1000)#ge signifcia que sea mayo o igual a 0. le indica menor o igual a 1000
    stock: int = Field(default=0, gt=0)#gt indico que el valor debe ser mayot a 0