import tkinter as tk

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
        textua.grid(row=0, column=1)
        textua2 = Label(root, text="Erabiltzailea:", width=20, font=("bold", 10))
        textua2.grid(row=1, column=0, sticky=E)
        izenaEntry = tk.Entry(root)
        izenaEntry.grid(row=1, column=1)
        izenak = Label(root)
        izenak.grid(row=2, column=1)
        textua = tk.Label(izenak, text="Erabiltzaileen izenak:").pack()
        res = Kontroladorea().erabiltzaileakPrintatuAdmin()
        for row in res:
            if row is not None:
                erab = str(row[0])
                erabil = tk.Label(izenak, text="(" + erab + ")").pack()

        ezabatu = tk.Button(root, text="Ezabatu", width=10, font=("bold", 10), bg='blue', command=ezabatu)
        ezabatu.grid(row=3, column=1, pady=10)
        amaitu = tk.Button(root, text="Amaitu", width=10, font=("bold", 10), bg='grey', command=atzera)
        amaitu.grid(row=4, column=1, pady=10)
        root.mainloop()