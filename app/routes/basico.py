import os
from starlette.responses import RedirectResponse
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse


from app.schemas import schema
router = APIRouter()

@router.get("/", include_in_schema=False)
def main():
    return RedirectResponse(url="/docs/")
   
@router.get("/retorna_nome/{nome}")
async def retorna_nome(nome: str):

    if nome:
        return JSONResponse(status_code=200, content={'[INFO]': 'Seja bem vindo '+nome+'!'})
    else:
        raise HTTPException(status_code=404, detail='Não colocou o nome!')    
        
@router.post("/descubra_nome_do_admin/")
async def descubra_nome_do_admin(key : schema.AccessKey ) :
    
    if key.access_key != os.getenv("ADMIN_USER", "admin"):
        raise HTTPException(status_code=401, detail='Access key negado.')

    return JSONResponse(status_code=200, content={'[INFO]': 'O nome do admin é Roberto!'})        
