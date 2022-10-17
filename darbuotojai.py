from darbuotojai_db import Darbuotojai, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from darbuotojai_db import *

session = sessionmaker(bind=engine)


def darbuotoju_sarasas():
    print("--- DARBUOTOJAI ---")
    darbuotojai = session.query(Darbuotojai).all()
    for darbuotojas in darbuotojai:
        print(darbuotojas)

def pasirinkimas():
    darbuotoju_sarasas()
    try:
        darbuotojo_id = int(input("Iveskite Darbuotojo ID: "))
    except ValueError:
        print("KLAIDA: ID privalo buti skaicius!")
        return None
    else:
        if darbuotojo_id:
            darbuotojas = session.query(Darbuotojai).get(darbuotojo_id)
            if darbuotojas:
                return darbuotojas
            else:
                print(f'KLAIDA: Darbuotojas su ID: {darbuotojo_id} neegzistuoja.')
                return None

def naujas_darbuotojas():
    print("--- NAUJAS DARBUOTOJAS ---")
    try:
        vardas = input("Vardas: ")
        pavarde = input("Pavarde: ")
        gimimo_data = datetime.strptime(input("Gimimo data YYYY-MM-DD: "), "%Y-%m-%d")
        pareigos = input("Pareigos: ")
        atlyginimas = float(input("Atlyginimas: "))
    except ValueError:
        print("KLAIDA!!!")
        return
    else:
        darbuotojas = Darbuotojai(vardas, pavarde, gimimo_data, pareigos, atlyginimas)
        session.add(darbuotojas)
        session.commit()
        print(f"Darbuotojas {vardas} buvo sekmingai iterptas i duomenu baze")


def darbuotojo_atnaujinimas():
    print("--- DARBUOTOJO INFO ATNAUJINIMAS ---")
    darbuotojas = pasirinkimas()
    if darbuotojas:
        try:
            vardas = input(f"Vardas ({darbuotojas.vardas}): ")
            pavarde = input(f"Pavarde ({darbuotojas.pavarde}): ")
            gimimo_data = input(f"Gimimo data ({darbuotojas.gimimo_data}): ")
            pareigos = input(f"Pareigos ({darbuotojas.pareigos}): ")
            atlyginimas = input(f"Atlyginimas ({darbuotojas.atlyginimas}): ")
        except ValueError:
            print("KLAIDA: Atlyginimas turi buti skaicius!")
        else:
            if len(vardas) > 0:
                darbuotojas.vardas = vardas
            if len(pavarde) > 0:
                darbuotojas.pavarde = pavarde
            if len(gimimo_data) == "%Y-%m-%d":
                darbuotojas.gimimo_data = gimimo_data
            if len(pareigos) > 0:
                darbuotojas.pareigos = pareigos
            if len(atlyginimas) > 0:
                darbuotojas.atlyginimas = atlyginimas
                session.commit()
                print(f"Darbuotojas {vardas} informacija buvo sekmingai atnaujinta.")



def darbuotojo_istrynimas():
    trinamas = pasirinkimas()
    if trinamas:
        session.delete(trinamas)
        session.commit()
        print(f"Darbuotojas {trinamas} buvo sekmingai istrintas.")
    else:
        print(f"KLAIDA: Darbuotojas su ID: {trinamas} neegzistuoja.")


while True:
    print("--- Darbuotojai ---")
    print("Pasirinkite veiksma:")
    print("d - Darbuotoju Sarasas")
    print("n - Naujo Darbuotojo Ivedimas")
    print("a - Darbuotojo Info Atnaujinimas")
    print("i - Darbuotojo Istrynimas")
    print("q - Iseiti")
    veiksmas = input("Prasome Pasirinkti:").casefold()
    if veiksmas == "d":
        darbuotoju_sarasas()
    elif veiksmas == "n":
        naujas_darbuotojas()
    elif veiksmas == "a":
        darbuotojo_atnaujinimas()
    elif veiksmas == "i":
        darbuotojo_istrynimas()
    elif veiksmas == "q":
        print("Programa Uzdaroma...")
        print("Viso gero!")
        break