import tkinter as tk
from model.DatuBase import *
from kontroladorea.Kontroladorea import *

class AdminLeioa(object):
    def __init__(self):
        super(AdminLeioa, self).__init__()
        root = tk.Tk()
        root.geometry('1000x2000')
        root.resizable(False, False)
        root.title("Admin leioa")

        def ezabatu():
            Kontroladorea().erabiltzaileaEzabatu(izenaEntry.get())
            root.destroy()

        def atzera():
            root.destroy()

        textua = tk.Label(root, text="Ezabatu erabiltzaileak", width=20, font=("bold", 20))
        textua.place(x=90, y=53)
        textua2 = Label(root, text="Erabiltzailea:", width=20, font=("bold", 10))
        textua2.place(x=90, y=90)
        izenaEntry = tk.Entry(root)
        izenaEntry.place(x=220,y= 90)
        izenak = Label(root)
        izenak.place(x=230,y=120)
        textua = tk.Label(izenak, text="Erabiltzaileen izenak:").pack()
        res = Kontroladorea().erabiltzaileakPrintatu()
        for row in res:
            if row is not None:
                erab = str(row[0])
                erabil = tk.Label(izenak, text="(" + erab + ")").pack()

        ezabatu = tk.Button(root, text="Ezabatu", width=10, font=("bold", 10), bg='blue', command=ezabatu)
        ezabatu.place(x=120, y=330)
        amaitu = tk.Button(root, text="Amaitu", width=10, font=("bold", 10), bg='grey', command=atzera)
        amaitu.place(x=220, y=330)
        root.mainloop()