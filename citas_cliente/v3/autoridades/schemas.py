"""
Autoridades V3, esquemas de pydantic
"""
from pydantic import BaseModel

from lib.schemas_base import OneBaseOut


class AutoridadOut(BaseModel):
    """Esquema para entregar autoridades"""

    id_hasheado: str | None
    clave: str | None
    descripcion: str | None
    descripcion_corta: str | None
    distrito_nombre: str | None

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class OneAutoridadOut(AutoridadOut, OneBaseOut):
    """Esquema para entregar una autoridad"""
