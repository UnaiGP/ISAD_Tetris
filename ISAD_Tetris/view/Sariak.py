import tkinter as tk
from kontroladorea.Kontroladorea import *

class Sariak(object):
    def __init__(self, erab):
        super(Sariak, self).__init__()
        self.window = tk.Tk()
        self.window.title("Sariak")

        def atzera():
            self.window.destroy()


        textua = tk.Label(self.window, text="SARIAK", width=20, font=("bold", 30))
        textua.grid(row=0, column=2)
        errazML = tk.Label(self.window, text="Erraza Master", width=20, font=("bold", 20))
        errazML.grid(row=1, column=0)
        ertainML = tk.Label(self.window, text="Ertaina Master", width=20, font=("bold", 20))
        ertainML.grid(row=1, column=1)
        zML = tk.Label(self.window, text="Zaila Master", width=20, font=("bold", 20))
        zML.grid(row=1, column=2)
        sML = tk.Label(self.window, text="Segidan Master", width=20, font=("bold", 20))
        sML.grid(row=1, column=3)
        tML = tk.Label(self.window, text="Top Master", width=20, font=("bold", 20))
        tML.grid(row=1, column=4)
        datuak=Kontroladorea().sariakLortu(erab)
        irabaziErraz = datuak[1]
        irabaziErtain = datuak[2]
        irabaziZail = datuak[3]
        segidan = datuak[14]
        top = datuak[15]
        print(irabaziErraz)
        if irabaziErraz >= 10:
            errazmaster = PhotoImage(master=self.window, file="./irudiak/sari10.png")
            errazmaste = Label(self.window, image=errazmaster)
            errazmaste.grid(row=2, column=0)
        elif irabaziErraz >= 5:
            errazmaster = PhotoImage(master=self.window, file="./irudiak/sari5.png")
            errazmaste = Label(self.window, image=errazmaster)
            errazmaste.grid(row=2, column=0)
        elif irabaziErraz >= 1:
            errazmaster = PhotoImage(master= self.window, file="./irudiak/sari1.png")
            errazmaste = Label(self.window, image=errazmaster)
            errazmaste.grid(row=2, column=0)

        if irabaziErtain >= 10:
            ertainmaster = PhotoImage(master=self.window, file="./irudiak/sari10.png")
            ertainmaste = Label(self.window, image=ertainmaster)
            ertainmaste.grid(row=2, column=1)
        elif irabaziErtain >= 5:
            ertainmaster = PhotoImage(master=self.window, file="./irudiak/sari5.png")
            ertainmaste = Label(self.window, image=ertainmaster)
            ertainmaste.grid(row=2, column=1)
        elif irabaziErtain >= 1:
            ertainmaster = PhotoImage(master= self.window, file="./irudiak/sari1.png")
            ertainmaste = Label(self.window, image=ertainmaster)
            ertainmaste.grid(row=2, column=1)

        if irabaziZail >= 10:
            zailmaster = PhotoImage(master=self.window, file="./irudiak/sari10.png")
            zailmaste = Label(self.window, image=zailmaster)
            zailmaste.grid(row=2, column=2)
        elif irabaziZail >= 5:
            zailmaster = PhotoImage(master=self.window, file="./irudiak/sari5.png")
            zailmaste = Label(self.window, image=zailmaster)
            zailmaste.grid(row=2, column=2)
        elif irabaziZail >= 1:
            zailmaster = PhotoImage(master= self.window, file="./irudiak/sari1.png")
            zailmaste = Label(self.window, image=zailmaster)
            zailmaste.grid(row=2, column=2)

        if segidan == 1:
            segimaster = PhotoImage(master=self.window, file="./irudiak/sariSegidan.png")
            segimaste = Label(self.window, image=segimaster)
            segimaste.grid(row=2, column=3)

        if top == 1:
            topmaster = PhotoImage(master=self.window, file="./irudiak/sariTop.png")
            topmaste = Label(self.window, image=topmaster)
            topmaste.grid(row=2, column=4)

        amaitu = tk.Button(self.window, text="Atzera", width=10, font=("bold", 10), bg='grey', command=atzera)
        amaitu.grid(row=3, column=2, pady=20)

        self.window.mainloop()