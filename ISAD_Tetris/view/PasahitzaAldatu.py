import tkinter as tk
from tkinter import *
import view.JokoHasiera
from kontroladorea.Kontroladorea import *
class PasahitzaAldatu:
    def __init__(self):
        root = tk.Tk()
        root.title("Pasahitz aldaketa")

        def aldatuPasahitza():
            if (izenaEntry.get() and pasahitzEntry.get() and berriaEntry.get()):
                if(Kontroladorea().aldatuPasahitza(izenaEntry.get(), pasahitzEntry.get(), berriaEntry.get())):
                    root.destroy()
                    view.JokoHasiera.JokoHasiera()
            else:
                showerror(title="ERROR", message="Informazioa falta da")

        def atzera():
            root.destroy()
            view.JokoHasiera.JokoHasiera()


        textua = Label(root, text="Zure datuak sartu", width=20, font=("bold", 20))
        textua.grid(row=0, column=1)
        izenaLabel = Label(root, text="Erabiltzaile izena:", width=20, font=("bold", 10))
        izenaLabel.grid(row=1, column=0, sticky=W, pady=10)
        izenaEntry = Entry(root)
        izenaEntry.grid(row=1, column=1, pady=10)
        pasahitzLabel = Label(root, text="Oraingo pasahitza:", width=20, font=("bold", 10))
        pasahitzLabel.grid(row=2, column=0, sticky=W, pady=10)
        pasahitzEntry = Entry(root)
        pasahitzEntry.grid(row=2, column=1, pady=10)
        berriaLabel = Label(root, text="Pasahitz berria:", width=20, font=("bold", 10))
        berriaLabel.grid(row=3, column=0, sticky=W, pady=10)
        berriaEntry = Entry(root)
        berriaEntry.grid(row=3, column=1, pady=10)
        Button(root, text='Aldatu', width=20, bg='blue', fg='white', command=aldatuPasahitza).grid(row=4, column=1, pady=10)
        atzeraBotoia = Button(root, text="Atzera", width=10, font=("bold", 10), bg='grey', command=atzera)
        atzeraBotoia.grid(row=5, column=1, pady=10)
        root.mainloop()