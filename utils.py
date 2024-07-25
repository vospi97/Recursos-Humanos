# utils.py
from datetime import date, timedelta
from sqlalchemy.orm import Session
from models import PeriodoFacturacion, EvaluacionDesempeno, Empleado
import random

def generar_periodo_facturacion(db: Session):
    today = date.today()
    if today.day <= 15:
        inicio_periodo = date(today.year, today.month, 1)
        final_periodo = date(today.year, today.month, 15)
    else:
        inicio_periodo = date(today.year, today.month, 16)
        final_periodo = date(today.year, today.month + 1, 1) - timedelta(days=1)

    periodo = PeriodoFacturacion(inicio_periodo=inicio_periodo, final_periodo=final_periodo)
    db.add(periodo)
    db.commit()
    db.refresh(periodo)
    return periodo

def generar_evaluaciones_quincenales(db: Session, periodo_id: int):
    empleados = db.query(Empleado).all()
    for empleado in empleados:
        calificacion = random.uniform(1, 10)  # Genera una calificación aleatoria entre 1 y 10
        evaluacion = EvaluacionDesempeno(id_empleado=empleado.id_empleado, id_periodo=periodo_id, calificacion=calificacion)
        db.add(evaluacion)
    db.commit()
