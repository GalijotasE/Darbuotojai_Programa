from darbuotojai_db import Darbuotojai
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from darbuotojai_db import Darbuotojai
from darbuotojai_programa import Darbuotojai


engine = create_engine('sqlite:///pirma.db')
Session = sessionmaker(bind=engine)
session = Session()

def database_sarasas():
    return session.query(Darbuotojai).all()


def prideti_prie_saraso(vardas, pavarde, gimimo_data, pareigos, atlyginimas):
    darbuotojas = Darbuotojai(vardas, pavarde, gimimo_data, pareigos, atlyginimas)
    session.add(darbuotojas)
    session.commit()

def istrinti_is_saraso(id):
    darbuotojai = session.query(Darbuotojai).get(id)
    session.delete(darbuotojai)
    session.commit()


def atnaujinti_duomenis(id, n_vardas, n_pavarde, n_gimimo_data, n_pareigos, n_atlyginimas):
    darbuotojai = session.query(Darbuotojai).get(id)
    darbuotojai.vardas = n_vardas
    darbuotojai.pavarde = n_pavarde
    darbuotojai.gimimo_data = n_gimimo_data
    darbuotojai.pareigos = n_pareigos
    darbuotojai.atlyginimas = n_atlyginimas
    session.commit()