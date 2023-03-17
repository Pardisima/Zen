import db
from sqlalchemy import Column, Integer, String, Boolean

class Tarea(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True) # Automaticamente esta PK se convertirá en SERIAL (AUTOINCREMENT)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)

    def __init__(self, contenido, hecha):
        self.contenido = contenido
        self.hecha = hecha

    def __repr__(self):
        return "Tarea({}: {}, {})".format(self.id, self.contenido, self.hecha)

    def __str__(self):
        return "Tarea({}: {}, {})".format(self.id, self.contenido, self.hecha)
