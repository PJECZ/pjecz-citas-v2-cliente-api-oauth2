"""
Pagos Pagos V3, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class PagoOut(BaseModel):
    """Esquema para entregar pagos"""

    id: int | None
    cit_cliente_id: int | None
    cit_cliente_nombre: str | None
    pag_tramite_servicio_id: int | None
    pag_tramite_servicio_clave: str | None
    pag_tramite_servicio_descripcion: str | None
    email: str | None
    estado: str | None
    folio: str | None
    total: float | None
    ya_se_envio_comprobante: bool | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OnePagoOut(PagoOut, OneBaseOut):
    """Esquema para entregar un pago"""


class PagCarroIn(BaseModel):
    """Esquema para recibir del carro de pagos"""

    nombres: str | None
    apellido_primero: str | None
    apellido_segundo: str | None
    curp: str | None
    email: str | None
    telefono: str | None
    pag_tramite_servicio_clave: str | None


class PagCarroOut(BaseModel):
    """Esquema para entregar al carro de pagos"""

    pag_pago_id: int | None
    descripcion: str | None
    email: str | None
    monto: float | None
    url: str | None


class OnePagCarroOut(PagCarroOut, OneBaseOut):
    """Esquema para entregar un pago"""


class PagResultadoIn(BaseModel):
    """Esquema para recibir del carro de pagos"""

    xml_encriptado: str | None


class PagResultadoOut(BaseModel):
    """Esquema para entregar al carro de pagos"""

    pag_pago_id: int | None
    nombres: str | None
    apellido_primero: str | None
    apellido_segundo: str | None
    email: str | None
    estado: str | None
    folio: str | None
    total: float | None


class OnePagResultadoOut(PagResultadoOut, OneBaseOut):
    """Esquema para entregar un pago"""
