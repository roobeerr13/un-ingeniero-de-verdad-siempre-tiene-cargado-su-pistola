import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear la base de datos SQLite
engine = create_engine('sqlite:///vectores.db', echo=False)
Base = declarative_base()

# Modelo para los resultados del Problema de las Reinas
class ReinasResult(Base):
    __tablename__ = 'reinas_results'
    id = Column(Integer, primary_key=True)
    tablero_size = Column(Integer, nullable=False)
    soluciones = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"ReinasResult(id={self.id}, tablero_size={self.tablero_size}, timestamp={self.timestamp})"

# Modelo para los resultados del Recorrido del Caballo
class CaballoResult(Base):
    __tablename__ = 'caballo_results'
    id = Column(Integer, primary_key=True)
    tablero_size = Column(Integer, nullable=False)
    start_x = Column(Integer, nullable=False)
    start_y = Column(Integer, nullable=False)
    recorrido = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"CaballoResult(id={self.id}, tablero_size={self.tablero_size}, start_x={self.start_x}, start_y={self.start_y}, timestamp={self.timestamp})"

# Modelo para los resultados de la Torre de Hanoi
class HanoiResult(Base):
    __tablename__ = 'hanoi_results'
    id = Column(Integer, primary_key=True)
    num_discos = Column(Integer, nullable=False)
    movimientos = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"HanoiResult(id={self.id}, num_discos={self.num_discos}, timestamp={self.timestamp})"

# Modelo para los vectores
class Vector(Base):
    __tablename__ = 'vectores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    datos = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Vector(id={self.id}, nombre={self.nombre}, datos={self.datos})"

# Crear todas las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)

def guardar_reinas_result(tablero_size, soluciones):
    session = Session()
    try:
        soluciones_json = json.dumps(soluciones)
        result = ReinasResult(tablero_size=tablero_size, soluciones=soluciones_json)
        session.add(result)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error al guardar resultado de Reinas: {e}")
    finally:
        session.close()

def mostrar_reinas_results():
    session = Session()
    try:
        resultados = session.query(ReinasResult).all()
        if not resultados:
            print("No hay resultados almacenados para el Problema de las Reinas.")
        else:
            for resultado in resultados:
                soluciones = json.loads(resultado.soluciones)
                print(f"ID: {resultado.id}, Tamaño del tablero: {resultado.tablero_size}, Fecha: {resultado.timestamp}")
                print(f"Primeras soluciones (máximo 1):")
                for i, solucion in enumerate(soluciones[:1]):
                    print(f"Solución {i + 1}: {solucion}")
                if len(soluciones) > 1:
                    print(f"(Y {len(soluciones) - 1} soluciones más...)")
                print()
    except Exception as e:
        print(f"Error al mostrar resultados de Reinas: {e}")
    finally:
        session.close()

def guardar_caballo_result(tablero_size, start_x, start_y, recorrido):
    session = Session()
    try:
        recorrido_json = json.dumps(recorrido)
        result = CaballoResult(tablero_size=tablero_size, start_x=start_x, start_y=start_y, recorrido=recorrido_json)
        session.add(result)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error al guardar resultado del Caballo: {e}")
    finally:
        session.close()

def mostrar_caballo_results():
    session = Session()
    try:
        resultados = session.query(CaballoResult).all()
        if not resultados:
            print("No hay resultados almacenados para el Recorrido del Caballo.")
        else:
            for resultado in resultados:
                recorrido = json.loads(resultado.recorrido)
                print(f"ID: {resultado.id}, Tamaño del tablero: {resultado.tablero_size}, Inicio: ({resultado.start_x}, {resultado.start_y}), Fecha: {resultado.timestamp}")
                print("Recorrido:")
                for fila in recorrido:
                    print(" ".join(f"{num:2}" for num in fila))
                print()
    except Exception as e:
        print(f"Error al mostrar resultados del Caballo: {e}")
    finally:
        session.close()

def guardar_hanoi_result(num_discos, movimientos):
    session = Session()
    try:
        movimientos_json = json.dumps(movimientos)
        result = HanoiResult(num_discos=num_discos, movimientos=movimientos_json)
        session.add(result)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error al guardar resultado de Hanoi: {e}")
    finally:
        session.close()

def mostrar_hanoi_results():
    session = Session()
    try:
        resultados = session.query(HanoiResult).all()
        if not resultados:
            print("No hay resultados almacenados para la Torre de Hanoi.")
        else:
            for resultado in resultados:
                movimientos = json.loads(resultado.movimientos)
                print(f"ID: {resultado.id}, Número de discos: {resultado.num_discos}, Fecha: {resultado.timestamp}")
                print(f"Movimientos (máximo 5 mostrados):")
                for mov in movimientos[:5]:
                    print(mov)
                if len(movimientos) > 5:
                    print(f"(Y {len(movimientos) - 5} movimientos más...)")
                print()
    except Exception as e:
        print(f"Error al mostrar resultados de Hanoi: {e}")
    finally:
        session.close()

def guardar_vector(nombre, elementos):
    session = Session()
    try:
        datos_json = json.dumps(elementos)
        vector = Vector(nombre=nombre, datos=datos_json)
        session.add(vector)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error al guardar el vector: {e}")
        return False
    finally:
        session.close()

def mostrar_vectores():
    session = Session()
    try:
        vectores = session.query(Vector).all()
        if not vectores:
            print("No hay vectores almacenados.")
        else:
            for vector in vectores:
                datos = json.loads(vector.datos)
                print(f"ID: {vector.id}, Nombre: {vector.nombre}, Datos: {datos}, Fecha: {vector.timestamp}")
    except Exception as e:
        print(f"Error al mostrar los vectores: {e}")
    finally:
        session.close()