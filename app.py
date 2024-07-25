# app.py
from fastapi import FastAPI
from routes import empleados, departamentos, contratos, nomina, asistencia

def create_app():
    app = FastAPI()

    app.include_router(empleados.router, prefix="/empleados", tags=["empleados"])
    app.include_router(departamentos.router, prefix="/departamentos", tags=["departamentos"])
    app.include_router(contratos.router, prefix="/contratos", tags=["contratos"])
    app.include_router(nomina.router, prefix="/nominas", tags=["nominas"])
    app.include_router(asistencia.router, prefix="/asistencias", tags=["asistencias"])

    return app


