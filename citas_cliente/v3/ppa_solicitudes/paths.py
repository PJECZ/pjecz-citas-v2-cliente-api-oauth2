"""
Pago de Pensiones Alimenticias - Solicitudes V3, rutas (paths)
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.exceptions import CitasAnyError

from .crud import get_ppa_solicitud
from .schemas import OnePpaSolicitudOut

ppa_solicitudes = APIRouter(prefix="/v3/ppa_solicitudes", tags=["pago de pensiones alimenticias"])


@ppa_solicitudes.get("/{ppa_solicitud_id_hasheado}", response_model=OnePpaSolicitudOut)
async def detalle_ppa_solicitud(
    ppa_solicitud_id_hasheado: str,
    db: Session = Depends(get_db),
):
    """Detalle de una solicitud a partir de su id hasheado"""
    try:
        ppa_solicitud = get_ppa_solicitud(
            db=db,
            ppa_solicitud_id_hasheado=ppa_solicitud_id_hasheado,
        )
    except CitasAnyError as error:
        return OnePpaSolicitudOut(success=False, message=str(error))
    return OnePpaSolicitudOut.from_orm(ppa_solicitud)
