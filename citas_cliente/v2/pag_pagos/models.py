"""
Pagos Pagos V2, modelos
"""
from collections import OrderedDict
from sqlalchemy import Boolean, Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class PagPago(Base, UniversalMixin):
    """PagPago"""

    # Nombre de la tabla
    __tablename__ = "pag_pagos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    fecha = Column(Date, index=True, nullable=False)
    descripcion = Column(String(256), nullable=False)
    archivo = Column(String(256), default="")
    url = Column(String(512), default="")

    def __repr__(self):
        """Representación"""
        return f"<PagPago {self.descripcion}>"
