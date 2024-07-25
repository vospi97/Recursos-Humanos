from sqlalchemy.orm import Session
from . import models, schemas

def get_empleados(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Empleado).offset(skip).limit(limit).all()
