import tkinter as tk
import view.Erregistroa
import view.SaioHasiera
import view.PasahitzBerreskurapena
import view.PasahitzaAldatu
from tkinter import *

class JokoHasiera(object):
    def __init__(self):
        self.interfazeaHasi()

    def interfazeaHasi(self):
        root = tk.Tk()
        root.resizable(False, False)
        root.title('Tetris')

        def saioaHasiClicked():
            root.destroy()
            view.SaioHasiera.SaioHasiera()

        def berreskurapenaClicked():
            root.destroy()
            view.PasahitzBerreskurapena.PasahitzBerreskurapena()

        def erregistroaClicked():
            root.destroy()
            view.Erregistroa.Erregistroa()

        def aldatuClicked():
            root.destroy()
            view.PasahitzaAldatu.PasahitzaAldatu()

        textua = Label(root, text="Zer egin nahi duzu?", width=20, font=("bold", 20))
        saioaHasiBotoia = Button(root, text='Saioa hasi', width=18, font=("bold", 10), bg = 'grey', command=saioaHasiClicked)
        berreskuratuPasahitzaBotoia = Button(root, text='Berreskuratu pasahitza', width=18, font=("bold", 10), bg = 'grey', command=berreskurapenaClicked)
        erregistratuBotoia = Button(root, text='Erregistratu erabiltzailea', width=18, font=("bold", 10), bg = 'grey', command=erregistroaClicked)
        pasahitzaAldatu = Button(root, text='Pasahitz aldaketa', width=18, font=("bold", 10), bg='grey', command=aldatuClicked)
        textua.grid(row = 0, column = 1, pady = 25)
        saioaHasiBotoia.grid(row = 1, column= 0, pady = 50, padx = 20)
        berreskuratuPasahitzaBotoia.grid(row = 1, column = 1, pady = 50)
        erregistratuBotoia.grid(row = 1, column = 2, pady = 50, sticky = W, padx = 20)
        pasahitzaAldatu.grid(row = 2, column = 1, pady = 20)
        root.mainloop()