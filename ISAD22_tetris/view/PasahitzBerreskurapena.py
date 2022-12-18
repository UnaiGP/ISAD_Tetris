import tkinter as tk
from tkinter import *
import view.JokoHasiera
from kontroladorea.Kontroladorea import *

class PasahitzBerreskurapena(object):
    def __init__(self):
        super(PasahitzBerreskurapena, self).__init__()
        root = tk.Tk()
        root.title("Pasahitz berreskurapena")

        def berreskurapena():
            if (izenaEntry.get()):
                Kontroladorea().pasahitzaBerreskuratu(izenaEntry.get())
            else:
                showerror(title="ERROR", message="Ez duzu sartu erabiltzailerik")

        def atzera():
            root.destroy()
            view.JokoHasiera.JokoHasiera()

        textuFaltsu= Label(root, text="", width=20, font=("bold", 20))
        textuFaltsu.grid(row = 0, column = 0, sticky = E, pady = 10)
        textuFaltsu.grid(row = 0, column = 0, sticky = E, pady = 10)
        textua = Label(root, text="Zure datuak sartu", width=20, font=("bold", 20))
        textua.place(x=160, y=33)
        izenaLabel = Label(root, text="Erabiltzaile izena:", width=20, font=("bold", 10))
        izenaLabel.grid(row = 1, column = 0, pady = 40, sticky = E, padx = 5)
        izenaEntry = Entry(root)
        izenaEntry.grid(row = 1, column = 1, sticky = W, pady = 10, padx = 5)
        botoia = Button(root, text='Berreskuratu', width=20, bg='blue', fg='white', command=berreskurapena)
        botoia.place(x = 250, y = 160)
        textuFaltsu2 = Label(root, text="", width=20, font=("bold", 20))
        textuFaltsu2.grid(row=3, column=1, sticky = E, pady=40)
        atzeraBotoia = Button(root, text="Atzera", width=10, font=("bold", 10), bg='grey', command=atzera)
        atzeraBotoia.place(x = 280, y = 200)
        root.mainloop()

