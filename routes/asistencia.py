from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import RegistroAsistencia
from schemas import AsistenciaCreate, Asistencia
from database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Asistencia)
def create_asistencia(asistencia: AsistenciaCreate, db: Session = Depends(get_db)):
    db_asistencia = RegistroAsistencia(**asistencia.dict())
    db.add(db_asistencia)
    db.commit()
    db.refresh(db_asistencia)
    return db_asistencia

@router.get("/", response_model=List[Asistencia])
def read_asistencia(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    asistencias = db.query(RegistroAsistencia).offset(skip).limit(limit).all()
    return asistencias

@router.get("/{asistencia_id}", response_model=Asistencia)
def read_asistencia(asistencia_id: int, db: Session = Depends(get_db)):
    asistencia = db.query(RegistroAsistencia).filter(RegistroAsistencia.id_asistencia == asistencia_id).first()
    if asistencia is None:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    return asistencia

@router.put("/{asistencia_id}", response_model=Asistencia)
def update_asistencia(asistencia_id: int, asistencia: AsistenciaCreate, db: Session = Depends(get_db)):
    db_asistencia = db.query(RegistroAsistencia).filter(RegistroAsistencia.id_asistencia == asistencia_id).first()
    if db_asistencia is None:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    for key, value in asistencia.dict().items():
        setattr(db_asistencia, key, value)
    db.commit()
    db.refresh(db_asistencia)
    return db_asistencia

@router.delete("/{asistencia_id}", response_model=Asistencia)
def delete_asistencia(asistencia_id: int, db: Session = Depends(get_db)):
    db_asistencia = db.query(RegistroAsistencia).filter(RegistroAsistencia.id_asistencia == asistencia_id).first()
    if db_asistencia is None:
        raise HTTPException(status_code=404, detail="Asistencia no encontrada")
    db.delete(db_asistencia)
    db.commit()
    return db_asistencia
