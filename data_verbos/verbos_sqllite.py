#verbos_sqllite.py
from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from data_verbos import verbos

# Usar sqlalchemy.orm.declarative_base() en lugar de sqlalchemy.ext.declarative.declarative_base()
Base = declarative_base()

# Definir el modelo Verbo
class Verbo(Base):
    __tablename__ = 'verbos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    kanji = Column(String, nullable=False)
    hiragana = Column(String, nullable=False)
    romaji = Column(String, nullable=False)
    es = Column(String, nullable=False)
    en = Column(String, nullable=False)

# Clase para la base de datos
class Database:
    def __init__(self, db_url='sqlite:///verbos.db'):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
    
    # Método para inicializar la base de datos si no existe
    def init_bd(self):
        Base.metadata.create_all(self.engine)

    # Método para inicializar la tabla de verbos
    def verbo_init(self):
        inspector = inspect(self.engine)
        if not inspector.has_table('verbos'):
            Base.metadata.tables['verbos'].create(self.engine)

    # Método para agregar verbos a la base de datos
    def add_verbos(self, verbos):
        session = self.Session()
        for verbo in verbos:
            nuevo_verbo = Verbo(**verbo)
            session.add(nuevo_verbo)
        session.commit()
        session.close()

# Crear una instancia de la base de datos
db = Database()

# Inicializar la base de datos y la tabla de verbos
db.init_bd()
db.verbo_init()

# Insertar los verbos en la base de datos
db.add_verbos(verbos)
