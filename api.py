from fastapi import FastAPI
from app.routes import basico

app = FastAPI(title="API de exemplo no FastAPI",
    description="API de exemplo para testar deploy via Gitlab",
    version="1.0.0")

app.include_router(basico.router,tags=['endpoints para teste'])

