import tkinter as tk
from view.JokatuLeioa import *
from kontroladorea.Kontroladorea import *

class PertsonalizazioLeioa(object):
    def __init__(self,erab):
        super(PertsonalizazioLeioa, self).__init__()
        root = tk.Tk()
        root.title("Pertsonalizatu")
        options1 = tk.StringVar(root)
        options1.set("Aukeratu")
        options2 = tk.StringVar(root)
        options2.set("Aukeratu")
        options3 = tk.StringVar(root)
        options3.set("Aukeratu")
        options4 = tk.StringVar(root)
        options4.set("Aukeratu")
        options5 = tk.StringVar(root)
        options5.set("Aukeratu")
        options6 = tk.StringVar(root)
        options6.set("Aukeratu")
        options7 = tk.StringVar(root)
        options7.set("Aukeratu")
        options8 = tk.StringVar(root)
        options8.set("Aukeratu")
        options9=tk.StringVar(root)
        options9.set("Aukeratu")


        def datuakGorde():
            if(options1.get() == "Aukeratu" or options2.get() == "Aukeratu" or options3.get() == "Aukeratu" or options4.get() == "Aukeratu"
            or options5.get() == "Aukeratu" or options6.get() == "Aukeratu" or options7.get() == "Aukeratu" or options8.get() == "Aukeratu"):
                showerror(title="BALIO OKERRA", message="Pertsonalizazio okerra (Aukeratu balio bat jasota)")
            else:

                Kontroladorea().setBackground(erab,options1.get())
                Kontroladorea().setSoinua(erab, options2.get())
                Kontroladorea().setLauki(erab,options3.get())
                Kontroladorea().setIlara(erab, options4.get())
                Kontroladorea().setL(erab,options5.get())
                Kontroladorea().setSLispilu(erab, options6.get())
                Kontroladorea().setZ(erab,options7.get())
                Kontroladorea().setZispilu(erab, options8.get())
                Kontroladorea().setT(erab,options9.get())
                showinfo(title="ONDO", message="Pertsonalizazioa gorde da, jokoa itxi aldaketak egiteko")

        def atzera():
            root.destroy()

        textuFaltsu = Label(root, text="", width=5, font=("bold", 20))
        textuFaltsu.grid(row=0, column=0, sticky=E, pady=10)

        textua = tk.Label(root, text="Pertsonalizazioa", width=20, font=("bold", 20))
        textua.place(x=1, y=5)

        background = Label(root, text="Background kolorea:", width=20, font=("bold", 10))
        background.grid(row=1, column=0, sticky=W)
        bakgroundKolorea = tk.OptionMenu(root, options1, 'Gorria','Marroia','Urdina','Berdea','Horia','Morea','Arrosa','Beltza','Zuria','Laranja','Gris')
        bakgroundKolorea.grid(row=1, column=1, sticky=E, padx= 20)

        soinua = Label(root, text="Soinua:", width=20, font=("bold", 10))
        soinua.grid(row=2, column=0, sticky=W)

        soinuAukera = tk.OptionMenu(root, options2, 'Soundtrack 1: Ballad of Godness','Soundtrack 2: Came And Get Your Love',
                                    'Soundtrack 3: Inazuma','Soundtrack 4: Platino','Soundtrack 5: Stars','Soundtrack 6: Tetris remix')
        soinuAukera.grid(row=2, column=1, sticky=E, padx= 20)

        laukia = Label(root, text="Lauki kolorea:", width=20, font=("bold", 10))
        laukia.grid(row=3, column=0, sticky=W)
        laukiaKolorea = tk.OptionMenu(root, options3, 'yellow','cyan','blue','green','red','purple','pink','black','orange','grey')
        laukiaKolorea.grid(row=3, column=1, sticky=E, padx= 20)

        ilara = Label(root, text="Ilara kolorea:", width=20, font=("bold", 10))
        ilara.grid(row=4, column=0, sticky=W)
        ilaraKolorea = tk.OptionMenu(root, options4, 'yellow','cyan','blue','green','red','purple','pink','black','orange','grey')
        ilaraKolorea.grid(row=4, column=1, sticky=E, padx= 20)

        l = Label(root, text="L kolorea:", width=20, font=("bold", 10))
        l.grid(row=5, column=0, sticky=W)
        lKolorea = tk.OptionMenu(root, options5, 'yellow','cyan','blue','green','red','purple','pink','black','orange','grey')
        lKolorea.grid(row=5, column=1, sticky=E, padx= 20)

        lIspilu = Label(root, text="L ispilu kolorea:", width=20, font=("bold", 10))
        lIspilu.grid(row=6, column=0, sticky=W)
        lIspiluKolorea = tk.OptionMenu(root, options6, 'yellow','cyan','blue','green','red','purple','pink','black','orange','grey')
        lIspiluKolorea.grid(row=6, column=1, sticky=E, padx= 20)

        z = Label(root, text="Z kolorea:", width=20, font=("bold", 10))
        z.grid(row=7, column=0, sticky=W)
        zKolorea = tk.OptionMenu(root, options7, 'yellow','cyan','blue','green','red','purple','pink','black','orange','grey')
        zKolorea.grid(row=7, column=1, sticky=E, padx= 20)

        zIspilu = Label(root, text="Z ispilu kolorea:", width=20, font=("bold", 10))
        zIspilu.grid(row=8, column=0, sticky=W)
        zIspiluKolorea = tk.OptionMenu(root, options8, 'yellow','cyan','blue','green','red','purple','pink','black','orange','grey')
        zIspiluKolorea.grid(row=8, column=1, sticky=E, padx= 20)

        t = Label(root, text="T kolorea:", width=20, font=("bold", 10))
        t.grid(row=9, column=0, sticky=W)
        tKolorea = tk.OptionMenu(root, options9, 'yellow', 'cyan', 'blue', 'green', 'red', 'purple', 'pink',
                                       'black', 'orange', 'grey')
        tKolorea.grid(row=9, column=1, sticky=E, padx= 20)

        textuFaltsu2 = Label(root, text="", width=10, font=("bold", 5))
        textuFaltsu2.grid(row=10, column=0, sticky=E, pady=30)

        gorde  = tk.Button(root, text="Gorde", width=10, font=("bold", 10), bg='grey', command=datuakGorde)
        gorde.place(x=50, y=370)

        amaitu = tk.Button(root, text="Amaitu", width=10, font=("bold", 10), bg='grey', command=atzera)
        amaitu.place(x=150, y=370)
        root.mainloop()