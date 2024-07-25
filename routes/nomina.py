from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import RegistroNomina
from schemas import NominaCreate, Nomina
from database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Nomina)
def create_nomina(nomina: NominaCreate, db: Session = Depends(get_db)):
    db_nomina = RegistroNomina(**nomina.model_dump())
    db.add(db_nomina)
    db.commit()
    db.refresh(db_nomina)
    return db_nomina

@router.get("/", response_model=List[Nomina])
def read_nominas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    nominas = db.query(RegistroNomina).offset(skip).limit(limit).all()
    return nominas

@router.get("/{nomina_id}", response_model=Nomina)
def read_nomina(nomina_id: int, db: Session = Depends(get_db)):
    nomina = db.query(RegistroNomina).filter(RegistroNomina.id_nomina == nomina_id).first()
    if nomina is None:
        raise HTTPException(status_code=404, detail="Nómina no encontrada")
    return nomina

@router.put("/{nomina_id}", response_model=Nomina)
def update_nomina(nomina_id: int, nomina: NominaCreate, db: Session = Depends(get_db)):
    db_nomina = db.query(RegistroNomina).filter(RegistroNomina.id_nomina == nomina_id).first()
    if db_nomina is None:
        raise HTTPException(status_code=404, detail="Nómina no encontrada")
    for key, value in nomina.model_dump().items():
        setattr(db_nomina, key, value)
    db.commit()
    db.refresh(db_nomina)
    return db_nomina

@router.delete("/{nomina_id}", response_model=Nomina)
def delete_nomina(nomina_id: int, db: Session = Depends(get_db)):
    db_nomina = db.query(RegistroNomina).filter(RegistroNomina.id_nomina == nomina_id).first()
    if db_nomina is None:
        raise HTTPException(status_code=404, detail="Nómina no encontrada")
    db.delete(db_nomina)
    db.commit()
    return db_nomina
