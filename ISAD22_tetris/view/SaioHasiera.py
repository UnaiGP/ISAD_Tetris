import tkinter as tk
from tkinter import *
from view.JokatuLeioa import *
import view.JokoHasiera
import view.ZailtasunMota
from kontroladorea.Kontroladorea import *

class SaioHasiera(object):
    def __init__(self):
        super(SaioHasiera, self).__init__()
        root = tk.Tk()
        root.title("Saio hasiera")

        def saioHasi():
            if (izenaEntry.get() and pasahitzEntry.get()):
                if (Kontroladorea.saioHasi(self, izenaEntry.get(), pasahitzEntry.get())):
                    erab = izenaEntry.get()
                    root.destroy()
                    view.ZailtasunMota.ZailtasunMota(erab)
            else:
                showerror(title="ERROR", message="Informazioa falta da")

        def atzera():
            root.destroy()
            view.JokoHasiera.JokoHasiera()

        textuFaltsu = Label(root, text="", width=20, font=("bold", 20))
        textuFaltsu.grid(row=0, column=0, sticky=E, pady=10)
        textua = Label(root, text="Zure datuak sartu", width=20, font=("bold", 20))
        textua.place(x=160, y=33)
        izenaLabel = Label(root, text="Erabiltzaile izena:", width=20, font=("bold", 10))
        izenaLabel.grid(row=1, column=0, sticky=E, pady=40)
        izenaEntry = Entry(root)
        izenaEntry.grid(row=1, column=1, sticky=W, pady=10)
        pasahitzLabel = Label(root, text="Pasahitza:", width=20, font=("bold", 10))
        pasahitzLabel.grid(row=2, column=0, sticky=E, pady=10)
        pasahitzEntry = Entry(root)
        pasahitzEntry.grid(row=2, column=1, sticky=W, pady=10)
        textuFaltsu2 = Label(root, text="", width=20, font=("bold", 20))
        textuFaltsu2.grid(row=3, column=1, sticky=E, pady=40)
        Button(root, text='Saioa hasi', width=20, bg='blue', fg='white', command=saioHasi).place(x = 250, y = 230)
        atzeraBotoia = Button(root, text="Atzera", width=10, font=("bold", 10), bg='grey', command=atzera)
        atzeraBotoia.place(x = 280, y = 260)
        root.mainloop()