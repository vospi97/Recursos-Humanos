from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Departamento
from schemas import DepartamentoCreate, Departamento
from database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Departamento)
def create_departamento(departamento: DepartamentoCreate, db: Session = Depends(get_db)):
    db_departamento = Departamento(**departamento.model_dump())
    db.add(db_departamento)
    db.commit()
    db.refresh(db_departamento)
    return db_departamento

@router.get("/", response_model=List[Departamento])
def read_departamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    departamentos = db.query(Departamento).offset(skip).limit(limit).all()
    return departamentos

@router.get("/{departamento_id}", response_model=Departamento)
def read_departamento(departamento_id: int, db: Session = Depends(get_db)):
    departamento = db.query(Departamento).filter(Departamento.id_departamento == departamento_id).first()
    if departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return departamento

@router.put("/{departamento_id}", response_model=Departamento)
def update_departamento(departamento_id: int, departamento: DepartamentoCreate, db: Session = Depends(get_db)):
    db_departamento = db.query(Departamento).filter(Departamento.id_departamento == departamento_id).first()
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    for key, value in departamento.model_dump().items():
        setattr(db_departamento, key, value)
    db.commit()
    db.refresh(db_departamento)
    return db_departamento

@router.delete("/{departamento_id}", response_model=Departamento)
def delete_departamento(departamento_id: int, db: Session = Depends(get_db)):
    db_departamento = db.query(Departamento).filter(Departamento.id_departamento == departamento_id).first()
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    db.delete(db_departamento)
    db.commit()
    return db_departamento
