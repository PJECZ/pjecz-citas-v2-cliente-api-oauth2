"""
Pagos Pagos v2, esquemas de pydantic
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PagPagoOut(BaseModel):
    """Esquema para entregar pagos"""

    id: int
    cit_cliente_id: int
    cit_cliente_nombre: str
    pag_tramite_servicio_id: int
    pag_tramite_servicio_clave: str
    pag_tramite_servicio_descripcion: str
    email: str
    estado: str
    folio: str
    resultado_tiempo: Optional[datetime] = None
    total: float
    ya_se_envio_comprobante: bool

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class PagCarroIn(BaseModel):
    """Esquema para recibir del carro de pagos"""

    nombres: str
    apellido_primero: str
    apellido_segundo: str
    curp: str
    email: str
    telefono: str
    pag_tramite_servicio_clave: str


class PagCarroOut(BaseModel):
    """Esquema para entregar al carro de pagos"""

    pag_pago_id: int
    descripcion: str
    email: str
    monto: float
    url: str


class PagResultadoIn(BaseModel):
    """Esquema para recibir del carro de pagos"""

    xml_encriptado: str


class PagResultadoOut(BaseModel):
    """Esquema para entregar al carro de pagos"""

    pag_pago_id: int
    nombres: str
    apellido_primero: str
    apellido_segundo: str
    email: str
    estado: str
    folio: str
    resultado_tiempo: Optional[datetime] = None
    total: float
