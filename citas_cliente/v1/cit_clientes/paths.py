"""
Cit Clientes v1, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from ..permisos.models import Permiso
from .authentications import get_current_active_user
from .crud import get_cit_clientes, get_cit_cliente
from .schemas import CitClienteInDB, CitClienteOut

cit_clientes = APIRouter(prefix="/v1/cit_clientes", tags=["clientes"])


@cit_clientes.get("", response_model=LimitOffsetPage[CitClienteOut])
async def listado_cit_clientes(
    current_user: CitClienteInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Listado de clientes"""
    if "CIT CLIENTES" not in current_user.permissions or current_user.permissions["CIT CLIENTES"] < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    return paginate(get_cit_clientes(db))


@cit_clientes.get("/{cit_cliente_id}", response_model=CitClienteOut)
async def detalle_cit_cliente(
    cit_cliente_id: int,
    current_user: CitClienteInDB = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Detalle de un cliente a partir de su id"""
    if "CIT CLIENTES" not in current_user.permissions or current_user.permissions["CIT CLIENTES"] < Permiso.VER:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
    try:
        cit_cliente = get_cit_cliente(db, cit_cliente_id)
    except IndexError as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Not acceptable: {str(error)}") from error
    return CitClienteOut.from_orm(cit_cliente)
