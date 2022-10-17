import tkinter as tk
from tkinter import *
from funkcijos import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///pirma.db')
Session = sessionmaker(bind=engine)
session = Session()

class Menu:
    def __init__(self, pagrindinis):
        self.pagrindinis = pagrindinis
        self.frame = tk.Frame(self.pagrindinis)
        self.pavadinimas = Label(pagrindinis, text= "=== DARBUOTOJAI ===", width=17, font=("Bahnschrift", 25))
        self.darbuotoju_sarasas = Button(pagrindinis, text="Darbuotoju Sarasas", command=self.sarasas, width=25, font=("Bahnschrift", 20))
        self.naujas_darbuotojas = Button(pagrindinis, text="Naujas Darbuotojas", command=self.naujas, width=25, font=("Bahnschrift", 20))
        self.darbuotojo_atnaujinimas = Button(pagrindinis, text="Atnaujinti Duomenis", width=25, font=("Bahnschrift", 20))
        self.darbuotojo_istrynimas = Button(pagrindinis, text="Istrinti Darbuotoja",command=self.istrynimas, width=25, font=("Bahnschrift", 20))
        self.iseiti = Button(pagrindinis, text="Iseiti",command=self.isejimas, width=25, font=("Bahnschrift", 20))
        self.pavadinimas.pack(side=TOP)
        self.darbuotoju_sarasas.pack(side=TOP)
        self.naujas_darbuotojas.pack(side=TOP)
        self.darbuotojo_atnaujinimas.pack(side=TOP)
        self.darbuotojo_istrynimas.pack(side=TOP)
        self.iseiti.pack(side=BOTTOM)
        self.frame.pack()

    def sarasas(self):
        self.newWindow = tk.Toplevel(self.pagrindinis)
        self.frame = tk.Frame(self.pagrindinis)
        self.app = self.newWindow
        self.newWindow.geometry("500x500")
        self.pavadinimas = Label(self.app, text="=== DARBUOTOJU SARASAS ===", font=("Bahnschrift", 25))
        self.sarasiukas = Listbox(self.app, height=400, width=450, selectmode=NONE)
        self.sarasiukas.insert(END, *database_sarasas())
        self.pavadinimas.pack(side=TOP)
        self.sarasiukas.pack(side=TOP)
        self.frame.pack()

    def naujas(self):
        self.newWindow = tk.Toplevel(self.pagrindinis)
        self.frame = tk.Frame(self.pagrindinis)
        self.app = self.newWindow
        self.newWindow.geometry("500x500")
        self.pavadinimas = Label(self.app, text="=== NAUJAS DARBUOTOJAS ===", font=("Bahnschrift", 25))
        self.u_vardas = Label(self.app, text="VARDAS",font=("Bahnschrift", 15))
        self.i_vardas = Entry(self.app)
        self.u_pavarde = Label(self.app, text="PAVARDE",font=("Bahnschrift", 15))
        self.i_pavarde = Entry(self.app)
        self.u_gimimo_data = Label(self.app, text="GIMIMO DATA YYYY-MM-DD",font=("Bahnschrift", 15))
        self.i_gimimo_data = Entry(self.app)
        self.u_pareigos = Label(self.app, text="PAREIGOS",font=("Bahnschrift", 15))
        self.i_pareigos = Entry(self.app)
        self.u_atlyginimas = Label(self.app, text="ATLYGINIMAS",font=("Bahnschrift", 15))
        self.i_atlyginimas = Entry(self.app)
        self.prideti = Button(self.app, text="PRIDETI", width=18, font=("Bahnschrift", 15))
        self.pavadinimas.pack(side=TOP)
        self.u_vardas.pack()
        self.i_vardas.pack()
        self.u_pavarde.pack()
        self.i_pavarde.pack()
        self.u_gimimo_data.pack()
        self.i_gimimo_data.pack()
        self.u_pareigos.pack()
        self.i_pareigos.pack()
        self.u_atlyginimas.pack()
        self.i_atlyginimas.pack()
        self.prideti.pack()
        self.frame.pack()
        

    def atnaujinimas(self):
        pass


    def istrynimas(self):
        self.newWindow = tk.Toplevel(self.pagrindinis)
        self.frame = tk.Frame(self.pagrindinis)
        self.app = self.newWindow
        self.newWindow.geometry("500x500")
        self.pavadinimas = Label(self.app, text="=== NAUJAS DARBUOTOJAS ===", font=("Bahnschrift", 25))
        self.pasirinkimas = Label(self.app, text="Pasirinkite Darbuotoja", font=("Bahnschrift", 15))
        self.pasirinkimas2 = Label(self.app, text="Kuri Norite Istrinti:", font=("Bahnschrift", 15))
        self.sarasiukas = Listbox(self.app, width=500 ,selectmode=SINGLE)
        self.sarasiukas.insert(END, *database_sarasas())
        self.istrinti = Button(self.app, text="ISTRINTI", font=("Bahnschrift", 15))
        #self.trinti = database_sarasas()[self.sarasiukas.curselection()[0]]
        #istrinti_is_saraso(id)
        self.pavadinimas.pack(side=TOP)
        self.pasirinkimas.pack(side=TOP)
        self.pasirinkimas2.pack(side=TOP)
        self.sarasiukas.pack(side=TOP)
        self.istrinti.pack(side=TOP)
        self.frame.pack()


    def isejimas(self):
        self.pagrindinis.destroy()

def pagrindinis_langas():
    langas = tk.Tk()
    app = Menu(langas)
    langas.geometry("500x500")
    langas.title("DARBUOTOJAI - DUOMENU BAZE")
    langas.mainloop()

if __name__ == '__main__':
    pagrindinis_langas()