from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
      
class AccessKey(BaseModel):
    access_key: str
 
 class Registros(BaseModel):
    id: int
    nome: str
    horario_consulta: datetime

    class Config:
        orm_mode = True