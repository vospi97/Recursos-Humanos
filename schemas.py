from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class EmpleadoBase(BaseModel):
    nombres: str
    apellidos: str
    cc: str
    fecha_nacimiento: date
    direccion: str
    telefono: str
    email: str
    tipo_sangre: Optional[str] = None

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoUpdate(EmpleadoBase):
    pass

class Empleado(EmpleadoBase):
    id_empleado: int

    class Config:
        from_attributes = True

class DepartamentoBase(BaseModel):
    nombre: str
    id_gerente: Optional[int] = None
    correo: Optional[str] = None
    telefono: Optional[str] = None

class DepartamentoCreate(DepartamentoBase):
    pass

class Departamento(DepartamentoBase):
    id_departamento: int

    class Config:
        from_attributes = True

class ContratoBase(BaseModel):
    id_empleado: int
    id_departamento: int
    fecha_inicio: date
    fecha_fin: Optional[date] = None
    tipo_contrato: str
    cargo: str
    salario_base: float
    email_empresarial: Optional[str] = None
    fecha_desvinculacion: Optional[date] = None
    eps: str
    arl: str
    pensiones: str

class ContratoCreate(ContratoBase):
    pass

class Contrato(ContratoBase):
    id_contrato: int

    class Config:
        from_attributes = True

class NominaBase(BaseModel):
    id_contrato: int
    fecha_pago: date
    salario_base: float
    deducciones: float
    salario_neto: float
    id_periodo: int

class NominaCreate(NominaBase):
    pass

class Nomina(NominaBase):
    id_nomina: int

    class Config:
        from_attributes = True

class AsistenciaBase(BaseModel):
    id_empleado: int
    observaciones: Optional[str] = None

class AsistenciaCreate(AsistenciaBase):
    pass

class Asistencia(AsistenciaBase):
    id_asistencia: int

    class Config:
        from_attributes = True
