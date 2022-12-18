import tkinter as tk
from tkinter import ttk
import model.DatuBase as DatuBase
import view.RankingMota as RankingMota
import view.JokatuLeioa as JokatuLeioa

from model.Tableroa import Tableroa


class Rankinga(object):
    def __init__(self, mota, erab):
        super(Rankinga, self).__init__()
        self.window = tk.Tk()
        self.window.geometry('900x900')
        if(mota == 2):
            self.window.title("Ranking pertsonala")
        else:
            self.window.title("Ranking")

        game_frame = tk.Frame(self.window)
        game_frame.pack()

        ranking = ttk.Treeview(game_frame)
        if mota==4 or mota==5 or mota==6:
            ranking['columns'] = ('Top', 'Erabiltzailea', 'Puntuazioa', 'Zailtasuna')
        else:
            ranking['columns'] = ('Top', 'Erabiltzailea', 'Puntuazioa')

        ranking.column("#0", width=0, stretch=False)
        ranking.column("Top", width=80)
        ranking.column("Erabiltzailea", width=100)
        ranking.column("Puntuazioa", width=100)
        if mota==4 or mota==5 or mota==6:
            ranking.column("Zailtasuna", width=100)
        ranking.heading("#0", text="")
        ranking.heading("Top", text="Top")
        ranking.heading("Erabiltzailea", text="Erabiltzailea")
        ranking.heading("Puntuazioa", text="Puntuazioa")
        if mota==4 or mota==5 or mota==6:
            ranking.heading("Zailtasuna", text="Zailtasuna")

        res = DatuBase.DatuBase.rankingPrintatu(self,mota,erab)
        top = 0;
        i=0
        if mota!=2:
            res1=res
            while i<len(res):
                a=str(res1[i])
                hitza=(a.translate({ord(','): None}))
                hitza = (hitza.translate({ord('('): None}))
                hitza = (hitza.translate({ord(')'): None}))
                hitza = hitza.replace("'","")
                res[i]=int(float(hitza))
                i=i+1

            res.sort(key=int)

        for row in res:
            if row is not None:
                top = top + 1
                erab = erab
                punt1=(res[0])
                punt2 = (res[1])
                punt3 = (res[2])
                punt4 = (res[3])
                punt5 = (res[4])
                punt6 = (res[5])
                punt7 = (res[6])
                punt8 = (res[7])
                punt9 = (res[8])
                punt10 =(res[9])


                """""""""
                punt2 = str(row[1])
                punt3 = str(row[2])
                punt4 = str(row[3])
                punt5 = str(row[4])
                punt6 = str(row[5])
                punt7 = str(row[6])
                punt8 = str(row[7])
                punt9 = str(row[8])
                punt10 = str(row[9])
                """""""""

        if mota==2:
            erabiltzaile1=erab
            erabiltzaile2 = erab
            erabiltzaile3 = erab
            erabiltzaile4 = erab
            erabiltzaile5 = erab
            erabiltzaile6 = erab
            erabiltzaile7 = erab
            erabiltzaile8 = erab
            erabiltzaile9 = erab
            erabiltzaile10 = erab
        elif mota==3:

            erabiltzaile1 = DatuBase.DatuBase.erabiltzaieakPrintatu(self,punt10)
            erabiltzaile2 = DatuBase.DatuBase.erabiltzaieakPrintatu(self,punt9)
            erabiltzaile3 = DatuBase.DatuBase.erabiltzaieakPrintatu(self,punt8)
            erabiltzaile4 = DatuBase.DatuBase.erabiltzaieakPrintatu(self,punt7)
            erabiltzaile5 = DatuBase.DatuBase.erabiltzaieakPrintatu(self,punt6)
            erabiltzaile6 = DatuBase.DatuBase.erabiltzaieakPrintatu(self,punt5)
            erabiltzaile7 = DatuBase.DatuBase.erabiltzaieakPrintatu(self,punt4)
            erabiltzaile8 = DatuBase.DatuBase.erabiltzaieakPrintatu(self,punt3)
            erabiltzaile9 = DatuBase.DatuBase.erabiltzaieakPrintatu(self,punt2)
            erabiltzaile10 = DatuBase.DatuBase.erabiltzaieakPrintatu(self,punt1)
        elif mota==4:
            erabiltzaile1 = DatuBase.DatuBase.erabiltzaieakPrinteatuErraza(self,punt10)
            erabiltzaile2 = DatuBase.DatuBase.erabiltzaieakPrinteatuErraza(self,punt9)
            erabiltzaile3 = DatuBase.DatuBase.erabiltzaieakPrinteatuErraza(self,punt8)
            erabiltzaile4 = DatuBase.DatuBase.erabiltzaieakPrinteatuErraza(self,punt7)
            erabiltzaile5 = DatuBase.DatuBase.erabiltzaieakPrinteatuErraza(self,punt6)
            erabiltzaile6 = DatuBase.DatuBase.erabiltzaieakPrinteatuErraza(self,punt5)
            erabiltzaile7 = DatuBase.DatuBase.erabiltzaieakPrinteatuErraza(self,punt4)
            erabiltzaile8 = DatuBase.DatuBase.erabiltzaieakPrinteatuErraza(self,punt3)
            erabiltzaile9 = DatuBase.DatuBase.erabiltzaieakPrinteatuErraza(self,punt2)
            erabiltzaile10 = DatuBase.DatuBase.erabiltzaieakPrinteatuErraza(self,punt1)
            zailtasuna1="ERRAZA"
            zailtasuna2 = "ERRAZA"
            zailtasuna3 = "ERRAZA"
            zailtasuna4 = "ERRAZA"
            zailtasuna5 = "ERRAZA"
            zailtasuna6 = "ERRAZA"
            zailtasuna7 = "ERRAZA"
            zailtasuna8 = "ERRAZA"
            zailtasuna9 = "ERRAZA"
            zailtasuna10 = "ERRAZA"
        elif mota==5:
            erabiltzaile1 = DatuBase.DatuBase.erabiltzaieakPrinteatuErtaina(self,punt10)
            erabiltzaile2 = DatuBase.DatuBase.erabiltzaieakPrinteatuErtaina(self,punt9)
            erabiltzaile3 = DatuBase.DatuBase.erabiltzaieakPrinteatuErtaina(self,punt8)
            erabiltzaile4 = DatuBase.DatuBase.erabiltzaieakPrinteatuErtaina(self,punt7)
            erabiltzaile5 = DatuBase.DatuBase.erabiltzaieakPrinteatuErtaina(self,punt6)
            erabiltzaile6 = DatuBase.DatuBase.erabiltzaieakPrinteatuErtaina(self,punt5)
            erabiltzaile7 = DatuBase.DatuBase.erabiltzaieakPrinteatuErtaina(self,punt4)
            erabiltzaile8 = DatuBase.DatuBase.erabiltzaieakPrinteatuErtaina(self,punt3)
            erabiltzaile9 = DatuBase.DatuBase.erabiltzaieakPrinteatuErtaina(self,punt2)
            erabiltzaile10 = DatuBase.DatuBase.erabiltzaieakPrinteatuErtaina(self,punt1)
            zailtasuna1 = "ERTAINA"
            zailtasuna2 = "ERTAINA"
            zailtasuna3 = "ERTAINA"
            zailtasuna4 = "ERTAINA"
            zailtasuna5 = "ERTAINA"
            zailtasuna6 = "ERTAINA"
            zailtasuna7 = "ERTAINA"
            zailtasuna8 = "ERTAINA"
            zailtasuna9 = "ERTAINA"
            zailtasuna10 = "ERTAINA"
        elif mota==6:
            erabiltzaile1 = DatuBase.DatuBase.erabiltzaieakPrinteatuZaila(self,punt10)
            erabiltzaile2 = DatuBase.DatuBase.erabiltzaieakPrinteatuZaila(self,punt9)
            erabiltzaile3 = DatuBase.DatuBase.erabiltzaieakPrinteatuZaila(self,punt8)
            erabiltzaile4 = DatuBase.DatuBase.erabiltzaieakPrinteatuZaila(self,punt7)
            erabiltzaile5 = DatuBase.DatuBase.erabiltzaieakPrinteatuZaila(self,punt6)
            erabiltzaile6 = DatuBase.DatuBase.erabiltzaieakPrinteatuZaila(self,punt5)
            erabiltzaile7 = DatuBase.DatuBase.erabiltzaieakPrinteatuZaila(self,punt4)
            erabiltzaile8 = DatuBase.DatuBase.erabiltzaieakPrinteatuZaila(self,punt3)
            erabiltzaile9 = DatuBase.DatuBase.erabiltzaieakPrinteatuZaila(self,punt2)
            erabiltzaile10 = DatuBase.DatuBase.erabiltzaieakPrinteatuZaila(self,punt1)
            zailtasuna1 = "ZAILA"
            zailtasuna2 = "ZAILA"
            zailtasuna3 = "ZAILA"
            zailtasuna4 = "ZAILA"
            zailtasuna5 = "ZAILA"
            zailtasuna6 = "ZAILA"
            zailtasuna7 = "ZAILA"
            zailtasuna8 = "ZAILA"
            zailtasuna9 = "ZAILA"
            zailtasuna10 = "ZAILA"

        if mota==2 or mota==3:

            ranking.insert(parent='', index='end', iid=0, text='',
                       values=(1, erabiltzaile1, punt10))
            ranking.insert(parent='', index='end', iid=1, text='',
                       values=(2, erabiltzaile2, punt9))
            ranking.insert(parent='', index='end', iid=2, text='',
                       values=(3, erabiltzaile3, punt8))
            ranking.insert(parent='', index='end', iid=3, text='',
                       values=(4, erabiltzaile4, punt7))
            ranking.insert(parent='', index='end', iid=4, text='',
                       values=(5, erabiltzaile5, punt6))
            ranking.insert(parent='', index='end', iid=5, text='',
                       values=(6, erabiltzaile6, punt5))
            ranking.insert(parent='', index='end', iid=6, text='',
                       values=(7, erabiltzaile7, punt4))
            ranking.insert(parent='', index='end', iid=7, text='',
                       values=(8, erabiltzaile8, punt3))
            ranking.insert(parent='', index='end', iid=8, text='',
                       values=(9, erabiltzaile9, punt2))
            ranking.insert(parent='', index='end', iid=9, text='',
                       values=(10, erabiltzaile10, punt1))
            ranking.pack()
        else:
            ranking.insert(parent='', index='end', iid=0, text='',
                           values=(1, erabiltzaile1, punt10, zailtasuna1))
            ranking.insert(parent='', index='end', iid=1, text='',
                           values=(2, erabiltzaile2, punt9, zailtasuna2))
            ranking.insert(parent='', index='end', iid=2, text='',
                           values=(3, erabiltzaile3, punt8, zailtasuna3))
            ranking.insert(parent='', index='end', iid=3, text='',
                           values=(4, erabiltzaile4, punt7, zailtasuna4))
            ranking.insert(parent='', index='end', iid=4, text='',
                           values=(5, erabiltzaile5, punt6, zailtasuna5))
            ranking.insert(parent='', index='end', iid=5, text='',
                           values=(6, erabiltzaile6, punt5, zailtasuna6))
            ranking.insert(parent='', index='end', iid=6, text='',
                           values=(7, erabiltzaile7, punt4, zailtasuna7))
            ranking.insert(parent='', index='end', iid=7, text='',
                           values=(8, erabiltzaile8, punt3, zailtasuna8))
            ranking.insert(parent='', index='end', iid=8, text='',
                           values=(9, erabiltzaile9, punt2, zailtasuna9))
            ranking.insert(parent='', index='end', iid=9, text='',
                           values=(10, erabiltzaile10, punt1, zailtasuna10))
            ranking.pack()

        amaitu = tk.Button(self.window, text="Atzera", width=10, font=("bold", 10), bg='grey', command=lambda:[RankingMota.RankingMota, self.window.destroy()])
        amaitu.pack()


        self.window.mainloop()