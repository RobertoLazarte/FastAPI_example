import os
import io
from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse, RedirectResponse
from fastapi import APIRouter, Form, Depends, HTTPException
from fastapi.responses import JSONResponse


from app.schemas import schema
from app.models import CRUDF, models
from app.models.database import SessionLocal, engine
 
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.get("/", include_in_schema=False)
def main():
    return RedirectResponse(url="/docs/")
   
@router.post("/retorna_nome/{nome}")
async def retorna_nome(nome: str, db: Session = Depends(get_db)):

    if nome:
        info_dict = {'nome':nome,'horario_consulta':datetime.now()}
        _ =  CRUDF.store_registro(db,info_dict)        
    
        return JSONResponse(status_code=201, content={'[INFO]': 'Registro do seguinte nome realizado no banco: '+nome+'!'})
    else:
        raise HTTPException(status_code=404, detail='Não colocou o nome!')    
        
@router.post("/descubra_nome_do_admin/")
async def descubra_nome_do_admin(key : schema.AccessKey ) :
    
    if key.access_key != os.getenv("ADMIN_USER", "admin"):
        raise HTTPException(status_code=401, detail='Access key negado.')

    return JSONResponse(status_code=200, content={'[INFO]': 'O nome do admin é Roberto!'})        
