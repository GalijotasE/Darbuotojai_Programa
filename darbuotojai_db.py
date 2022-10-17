import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///pirma.db')
Base = declarative_base()

class Darbuotojai(Base):
    __tablename__ = 'Darbuotojai'
    id = Column(Integer, primary_key = True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavarde", String)
    gimimo_data = Column("Gimimo Data", DateTime)
    pareigos = Column("Pareigos", String)
    atlyginimas = Column("Atlyginimas", Float)
    dirba_nuo = Column("Dirba nuo", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, vardas, pavarde, gimimo_data, pareigos, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas
    
    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.gimimo_data}, {self.pareigos}, {self.atlyginimas}, {self.dirba_nuo})"

Base.metadata.create_all(engine)