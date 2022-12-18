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
                if(Kontroladorea.aldatuPasahitza(self, izenaEntry.get(), pasahitzEntry.get(), berriaEntry.get())):
                    root.destroy()
                    view.JokoHasiera.JokoHasiera()
            else:
                showerror(title="ERROR", message="Informazioa falta da")

        def atzera():
            root.destroy()
            view.JokoHasiera.JokoHasiera()

        textuFaltsu = Label(root, text="", width=20, font=("bold", 20))
        textuFaltsu.grid(row=0, column=0, sticky=E, pady=10)
        textua = Label(root, text="Zure datuak sartu", width=20, font=("bold", 20))
        textua.place(x=160, y=13)
        izenaLabel = Label(root, text="Erabiltzaile izena:", width=20, font=("bold", 10))
        izenaLabel.grid(row=1, column=0, sticky=E, pady=10)
        izenaEntry = Entry(root)
        izenaEntry.grid(row=1, column=1, sticky=W, pady=10)
        pasahitzLabel = Label(root, text="Oraingo pasahitza:", width=20, font=("bold", 10))
        pasahitzLabel.grid(row=2, column=0, sticky=E, pady=10)
        pasahitzEntry = Entry(root)
        pasahitzEntry.grid(row=2, column=1, sticky=W, pady=10)
        berriaLabel = Label(root, text="Pasahitz berria:", width=20, font=("bold", 10))
        berriaLabel.grid(row=3, column=0, sticky=E, pady=10)
        berriaEntry = Entry(root)
        berriaEntry.grid(row=3, column=1, sticky=W, pady=10)
        textuFaltsu2 = Label(root, text="", width=20, font=("bold", 20))
        textuFaltsu2.grid(row=5, column=1, sticky=E, pady=40)
        Button(root, text='Aldatu', width=20, bg='blue', fg='white', command=aldatuPasahitza).place(x = 250, y = 210)
        atzeraBotoia = Button(root, text="Atzera", width=10, font=("bold", 10), bg='grey', command=atzera)
        atzeraBotoia.place(x = 280, y = 240)
        root.mainloop()