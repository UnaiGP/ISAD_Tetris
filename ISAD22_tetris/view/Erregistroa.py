import tkinter as tk
from tkinter import *
from model.DatuBase import *
import view.JokoHasiera
from kontroladorea.Kontroladorea import *

class Erregistroa:
    def __init__(self):
        root = tk.Tk()
        root.resizable(True, True)
        root.title("Erregistroa")

        def erregistroa():
            if (izenaEntry.get() and pasahitzEntry.get() and errepikapenaEntry.get()):
                if (pasahitzEntry.get() == errepikapenaEntry.get()):
                    if (Kontroladorea().erregistroa(izenaEntry.get(), pasahitzEntry.get())):
                        root.destroy()
                        view.JokoHasiera.JokoHasiera()
                else:
                    showerror(title="ERROR", message="Pasahitzak ez dira berdinak")
            else:
                showerror(title="ERROR", message="Informazioa falta da")

        def atzera():
            root.destroy()
            view.JokoHasiera.JokoHasiera()

        textuaFALTSUA = Label(root, text=" ", width=20, font=("bold", 20))
        textua = Label(root, text="Zure datuak sartu", width=20, font=("bold", 20))
        izenaLabel = Label(root, text="Erabiltzaile izena:", width=20, font=("bold", 10))
        izenaEntry = Entry(root)
        pasahitzLabel = Label(root, text="Pasahitza:", width=20, font=("bold", 10))
        pasahitzEntry = Entry(root)
        errepikapenaLabel = Label(root, text="Pasahitza errepikatu:", width=20, font=("bold", 10))
        errepikapenaEntry = Entry(root)
        atzeraBotoiFaltsua = Label(root, text=" ", width=20, font=("bold", 20))
        erregis = Button(root, text='Erregistratu', width=20, bg='blue', fg='white', command=erregistroa)
        atzeraBotoia = Button(root, text="Atzera", width=10, font=("bold", 10), bg='grey', command=atzera)
        textuaFALTSUA.grid(row = 0, column=1, padx=10)
        textua.place(x = 25, y = 10)
        izenaLabel.grid(row = 1, column = 0, sticky = W, pady = 25)
        izenaEntry.grid(row = 1, column = 1, sticky = W, pady = 25)
        pasahitzLabel.grid(row = 2, column = 0, sticky = W, pady = 25)
        pasahitzEntry.grid(row = 2, column = 1, sticky = W, pady = 25)
        errepikapenaLabel.grid(row = 3, column = 0, sticky = W, pady = 25)
        errepikapenaEntry.grid(row = 3, column = 1, sticky = W, pady = 25)
        atzeraBotoiFaltsua.grid(row = 5, column = 1, sticky = W, pady = 25)
        erregis.place(x=120, y = 270)
        atzeraBotoia.place(x=150, y = 300)
        root.mainloop()