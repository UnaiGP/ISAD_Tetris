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

        textua = Label(root, text="Zure datuak sartu", width=20, font=("bold", 20))
        textua.grid(row=0, column=1)
        izenaLabel = Label(root, text="Erabiltzaile izena:", width=20, font=("bold", 10))
        izenaLabel.grid(row = 1, column = 0, pady = 40, sticky =W, padx = 5)
        izenaEntry = Entry(root)
        izenaEntry.grid(row = 1, column = 1, pady = 10, padx = 5)
        botoia = Button(root, text='Berreskuratu', width=20, bg='blue', fg='white', command=berreskurapena)
        botoia.grid(row=2, column=1, pady=10)
        atzeraBotoia = Button(root, text="Atzera", width=10, font=("bold", 10), bg='grey', command=atzera)
        atzeraBotoia.grid(row=3, column=1, pady=10)
        root.mainloop()

