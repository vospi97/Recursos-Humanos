from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Contrato
from schemas import ContratoCreate, Contrato
from database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=Contrato)
def create_contrato(contrato: ContratoCreate, db: Session = Depends(get_db)):
    db_contrato = Contrato(**contrato.dict())
    db.add(db_contrato)
    db.commit()
    db.refresh(db_contrato)
    return db_contrato

@router.get("/", response_model=List[Contrato])
def read_contratos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    contratos = db.query(Contrato).offset(skip).limit(limit).all()
    return contratos

@router.get("/{contrato_id}", response_model=Contrato)
def read_contrato(contrato_id: int, db: Session = Depends(get_db)):
    contrato = db.query(Contrato).filter(Contrato.id_contrato == contrato_id).first()
    if contrato is None:
        raise HTTPException(status_code=404, detail="Contrato no encontrado")
    return contrato

@router.put("/{contrato_id}", response_model=Contrato)
def update_contrato(contrato_id: int, contrato: ContratoCreate, db: Session = Depends(get_db)):
    db_contrato = db.query(Contrato).filter(Contrato.id_contrato == contrato_id).first()
    if db_contrato is None:
        raise HTTPException(status_code=404, detail="Contrato no encontrado")
    for key, value in contrato.dict().items():
        setattr(db_contrato, key, value)
    db.commit()
    db.refresh(db_contrato)
    return db_contrato

@router.delete("/{contrato_id}", response_model=Contrato)
def delete_contrato(contrato_id: int, db: Session = Depends(get_db)):
    db_contrato = db.query(Contrato).filter(Contrato.id_contrato == contrato_id).first()
    if db_contrato is None:
        raise HTTPException(status_code=404, detail="Contrato no encontrado")
    db.delete(db_contrato)
    db.commit()
    return db_contrato
