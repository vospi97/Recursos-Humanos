from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Empleado
from schemas import EmpleadoBase, EmpleadoUpdate, EmpleadoCreate, Empleado
from database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Empleado)
def create_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_db)):
    db_empleado = Empleado(**empleado.dict())
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

@router.get("/", response_model=List[Empleado])
def read_empleados(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    empleados = db.query(Empleado).offset(skip).limit(limit).all()
    return empleados

@router.get("/{empleado_id}", response_model=Empleado)
def read_empleado(empleado_id: int, db: Session = Depends(get_db)):
    empleado = db.query(Empleado).filter(Empleado.id_empleado == empleado_id).first()
    if empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

@router.put("/{empleado_id}", response_model=Empleado)
def update_empleado(empleado_id: int, empleado: EmpleadoUpdate, db: Session = Depends(get_db)):
    db_empleado = db.query(Empleado).filter(Empleado.id_empleado == empleado_id).first()
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    for key, value in empleado.dict().items():
        setattr(db_empleado, key, value)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

@router.delete("/{empleado_id}", response_model=Empleado)
def delete_empleado(empleado_id: int, db: Session = Depends(get_db)):
    db_empleado = db.query(Empleado).filter(Empleado.id_empleado == empleado_id).first()
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    db.delete(db_empleado)
    db.commit()
    return db_empleado
