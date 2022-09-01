"""
Citas V2 API OAuth2
"""
from datetime import timedelta

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_pagination import add_pagination
from sqlalchemy.orm import Session

from config.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from lib.database import get_db

from citas_cliente.v2.autoridades.paths import autoridades
from citas_cliente.v2.cit_citas.paths import cit_citas
from citas_cliente.v2.cit_clientes.paths import cit_clientes
from citas_cliente.v2.cit_clientes_recuperaciones.paths import cit_clientes_recuperaciones
from citas_cliente.v2.cit_clientes_registros.paths import cit_clientes_registros
from citas_cliente.v2.cit_dias_disponibles.paths import cit_dias_disponibles
from citas_cliente.v2.cit_horas_disponibles.paths import cit_horas_disponibles
from citas_cliente.v2.cit_oficinas_servicios.paths import cit_oficinas_servicios
from citas_cliente.v2.cit_pagos.paths import cit_pagos
from citas_cliente.v2.cit_servicios.paths import cit_servicios
from citas_cliente.v2.cit_tramites_servicios.paths import cit_tramites_servicios
from citas_cliente.v2.distritos.paths import distritos
from citas_cliente.v2.domicilios.paths import domicilios
from citas_cliente.v2.enc_servicios.paths import enc_servicios
from citas_cliente.v2.enc_sistemas.paths import enc_sistemas
from citas_cliente.v2.materias.paths import materias
from citas_cliente.v2.oficinas.paths import oficinas

from citas_cliente.v2.cit_clientes.authentications import authenticate_user, create_access_token, get_current_active_user
from citas_cliente.v2.cit_clientes.schemas import Token, CitClienteInDB

try:
    from instance.settings import ORIGINS
except ImportError:
    from config.settings import ORIGINS

# FastAPI
app = FastAPI(
    title="Citas V2 API OAuth2",
    description="API del Sistema de Citas V2 del Poder Judicial del Estado de Coahuila de Zaragoza",
)

# CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths
app.include_router(autoridades)
app.include_router(cit_citas)
app.include_router(cit_clientes)
app.include_router(cit_clientes_recuperaciones)
app.include_router(cit_clientes_registros)
app.include_router(cit_dias_disponibles)
app.include_router(cit_horas_disponibles)
app.include_router(cit_oficinas_servicios)
app.include_router(cit_pagos)
app.include_router(cit_servicios)
app.include_router(cit_tramites_servicios)
app.include_router(distritos)
app.include_router(domicilios)
app.include_router(enc_servicios)
app.include_router(enc_sistemas)
app.include_router(materias)
app.include_router(oficinas)

# Pagination
add_pagination(app)


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Bienvenido a Citas V2 API OAuth2 del Poder Judicial del Estado de Coahuila de Zaragoza."}


@app.post("/token", response_model=Token)
@app.post("/v2/token", response_model=Token)
async def ingresar_para_solicitar_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Entregar el token como un JSON"""
    cit_cliente = authenticate_user(form_data.username, form_data.password, db)
    if not cit_cliente:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": cit_cliente.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer", "username": cit_cliente.username}


@app.get("/profile", response_model=CitClienteInDB)
@app.get("/v2/profile", response_model=CitClienteInDB)
async def mi_perfil(current_user: CitClienteInDB = Depends(get_current_active_user)):
    """Mostrar el perfil del cliente"""
    return current_user
