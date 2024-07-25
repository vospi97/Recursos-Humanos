from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empleado(Base):
    __tablename__ = 'empleados'
    id_empleado = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(100))
    apellidos = Column(String(100))
    cc = Column(String(50), unique=True)
    fecha_nacimiento = Column(Date)
    direccion = Column(String(200))
    telefono = Column(String(20))
    email = Column(String(100))
    tipo_sangre = Column(String(10))

class Departamento(Base):
    __tablename__ = 'departamentos'
    id_departamento = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    id_gerente = Column(Integer, ForeignKey('empleados.id_empleado'))
    correo = Column(String(100))
    telefono = Column(String(20))

class Contrato(Base):
    __tablename__ = 'contratos'
    id_contrato = Column(Integer, primary_key=True, index=True)
    id_empleado = Column(Integer, ForeignKey('empleados.id_empleado'))
    id_departamento = Column(Integer, ForeignKey('departamentos.id_departamento'))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    tipo_contrato = Column(String(50))
    cargo = Column(String(100))
    salario_base = Column(DECIMAL(10, 2))
    email_empresarial = Column(String(100))
    fecha_desvinculacion = Column(Date)
    eps = Column(String(100))
    arl = Column(String(100))
    pensiones = Column(String(100))

class PeriodoFacturacion(Base):
    __tablename__ = 'periodo_facturacion'
    id_periodo = Column(Integer, primary_key=True, index=True)
    inicio_periodo = Column(Date)
    final_periodo = Column(Date)

class RegistroNomina(Base):
    __tablename__ = 'registro_nomina'
    id_nomina = Column(Integer, primary_key=True, index=True)
    id_contrato = Column(Integer, ForeignKey('contratos.id_contrato'))
    fecha_pago = Column(Date)
    salario_base = Column(DECIMAL(10, 2))
    deducciones = Column(DECIMAL(10, 2))
    salario_neto = Column(DECIMAL(10, 2))
    id_periodo = Column(Integer, ForeignKey('periodo_facturacion.id_periodo'))

class EvaluacionDesempeno(Base):
    __tablename__ = 'evaluacion_desempeno'
    id_evaluacion = Column(Integer, primary_key=True, index=True)
    id_empleado = Column(Integer, ForeignKey('empleados.id_empleado'))
    id_periodo = Column(Integer, ForeignKey('periodo_facturacion.id_periodo'))
    calificacion = Column(DECIMAL(3, 2))

class RegistroAsistencia(Base):
    __tablename__ = 'registro_asistencia'
    id_asistencia = Column(Integer, primary_key=True, index=True)
    id_empleado = Column(Integer, ForeignKey('empleados.id_empleado'))
    observaciones = Column(String)
