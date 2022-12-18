import random
import tkinter as tk
from model.Tableroa import Tableroa
from model.Piezak import *
from view.JokatuLeioa import *

class ZailtasunMota(object):
    def __init__(self, erab):
        super(ZailtasunMota, self).__init__()
        self.window = tk.Tk()
        self.window.title("Zailtasuna aukeratu")

        label=tk.Label(self.window, text="Aukeratu zailtasun maila",  width=20, font=("bold", 20))
        label.place(x=5, y=50);

        button1 = tk.Button(self.window, text="ERRAZA", bg='grey',command=lambda:[self.window.destroy(),JokatuLeioa(1, erab)]).grid(row = 0, column= 0, pady=100, padx = 30)
        button2 = tk.Button(self.window, text="ERTAINA", bg='grey', command=lambda:[self.window.destroy(),JokatuLeioa(2, erab)]).grid(row = 0, column= 1, pady=100, padx = 30)
        button3= tk.Button(self.window, text="ZAILA", bg='grey', command=lambda:[self.window.destroy(),JokatuLeioa(3, erab)]).grid(row = 0, column= 2, pady=100, padx = 30)


        self.window.mainloop()

