from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import close_connection, connect
from .transporte.router import router as TransporteRouter
from decouple import config
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifeSpan(app: FastAPI):
    await connect()
    yield
    await close_connection()




app = FastAPI(lifespan=lifeSpan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los encabezados
)
app.include_router(TransporteRouter)

