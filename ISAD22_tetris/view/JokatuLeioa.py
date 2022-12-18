import multiprocessing
import pygame
from pygame.locals import *
from pygame import mixer
from playsound import playsound
from threading import Thread
import random
import tkinter as tk
import view.AdminLeioa
import view.RankingMota
from model.Tableroa import Tableroa
from model.Piezak import *
from view.AdminLeioa import AdminLeioa
from view.PertsonalizazioLeioa import PertsonalizazioLeioa
from view.Sariak import Sariak
from model.DatuBase import *
from kontroladorea.Kontroladorea import *
from irudiak import *

class JokatuLeioa(object):

    def __init__(self,x, erab):
        super(JokatuLeioa, self).__init__()
        self.window = tk.Tk()
        self.window.title("Tetris jokoa")
        if Kontroladorea().musikaLortu(erab) != "default":
            if(Kontroladorea().backgroundLortu(erab) == 'Gorria'):
                self.window['bg'] = 'red'
            if(Kontroladorea().backgroundLortu(erab) == 'Marroia'):
                self.window['bg'] = 'brown'
            if (Kontroladorea().backgroundLortu(erab) == 'Urdina'):
                self.window['bg'] = 'blue'
            if (Kontroladorea().backgroundLortu(erab) == 'Berdea'):
                self.window['bg'] = 'green'
            if (Kontroladorea().backgroundLortu(erab) == 'Horia'):
                self.window['bg'] = 'yellow'
            if (Kontroladorea().backgroundLortu(erab) == 'Morea'):
                self.window['bg'] = 'purple'
            if (Kontroladorea().backgroundLortu(erab) == 'Arrosa'):
                self.window['bg'] = 'pink'
            if (Kontroladorea().backgroundLortu(erab) == 'Beltza'):
                self.window['bg'] = 'black'
            if (Kontroladorea().backgroundLortu(erab) == 'Zuria'):
                self.window['bg'] = 'white'
            if (Kontroladorea().backgroundLortu(erab) == 'Laranja'):
                self.window['bg'] = 'orange'
            if (Kontroladorea().backgroundLortu(erab) == 'Gris'):
                self.window['bg'] = 'grey'
        self.x=x
        self.erab=erab

        def adminLeioa():
            view.AdminLeioa.AdminLeioa()

        def pertsoLeioa():
            view.PertsonalizazioLeioa.PertsonalizazioLeioa(erab)

        def ranking():
            view.RankingMota.RankingMota(erab)

        def sariak():
            view.Sariak.Sariak(erab)

        def atzera():
            self.window.destroy()
            view.ZailtasunMota.ZailtasunMota(erab)

        button = tk.Button(self.window, text="Partida hasi")
        button.grid(row=0, column=0)

        puntuazioa = tk.StringVar()
        puntuazioa.set("Puntuazioa: 0")

        puntuazioalabel = tk.Label(self.window, textvariable=puntuazioa)
        puntuazioalabel.grid(row=1, column=0)

        gorde = tk.Button(self.window, text="Gorde partida", state=DISABLED)
        gorde.grid(row=2, column=0)

        kargatu = tk.Button(self.window, text="Kargatu partida", state=DISABLED)
        kargatu.grid(row=3, column=0)

        ranking = tk.Button(self.window, text="Rankin", command=ranking)
        ranking.grid(row=0, column=1, sticky=W)
        sariak = tk.Button(self.window, text="Sariak", command=sariak)
        sariak.grid(row=1, column=1, sticky=E)
        amaitu = tk.Button(self.window, text="Atzera", command=atzera)
        amaitu.grid(row=2, column=1, sticky=E)

        if (erab == 'Admin'):
            admin = tk.Button(self.window, text="Admin", command=adminLeioa)
            admin.grid(row=5, column=0, sticky=W)

        pertso = tk.Button(self.window, text="Pertsonalizazioa",command=pertsoLeioa)
        pertso.grid(row=6, column=0)

        if x==1:
            canvas = TableroaPanela(1,(15,20),button,gorde,kargatu,erab,master=self.window, puntuazioalabel=puntuazioa)
            button.configure(command=canvas.jolastu)
            canvas.grid(row=7, column=0, sticky=W)
        elif x==2:
            canvas = TableroaPanela(2,(10,20),button,gorde,kargatu,erab,master=self.window, puntuazioalabel=puntuazioa)
            button.configure(command=canvas.jolastu)
            canvas.grid(row=7, column=0, sticky=W)
        elif x == 3:
            canvas = TableroaPanela(3,(10,15),button,gorde,kargatu,erab,master=self.window, puntuazioalabel=puntuazioa)
            button.configure(command=canvas.jolastu)
            canvas.grid(row=7, column=0, sticky=W)

        self.window.bind("<Up>", canvas.joku_kontrola)
        self.window.bind("<Down>", canvas.joku_kontrola)
        self.window.bind("<Right>", canvas.joku_kontrola)
        self.window.bind("<Left>", canvas.joku_kontrola)

        self.window.mainloop()



class TableroaPanela(tk.Frame):
    def __init__(self,zailtasun, tamaina,button,gorde,kargatu, erab,gelazka_tamaina=20, puntuazioalabel=None, master=None):
        tk.Frame.__init__(self, master)
        self.puntuazio_panela = puntuazioalabel
        self.tamaina = tamaina
        self.gelazka_tamaina = gelazka_tamaina
        self.zailtasuna=zailtasun
        self.erab=erab
        self.button = button
        self.gorde = gorde
        self.kargatu = kargatu
        self.kargatu.configure(state=ACTIVE, command=self.lortuTableroa)

        self.canvas = tk.Canvas(
            width=self.tamaina[0] * self.gelazka_tamaina + 1,
            height=self.tamaina[1] * self.gelazka_tamaina + 1,
            bg='#eee', borderwidth=0, highlightthickness=0
        )
        self.canvas.grid()

        self.tab = Tableroa(tamaina,zailtasun)
        self.jokatzen = None
        self.tableroa_ezabatu()

    def marratu_gelazka(self, x, y, color):
        self.canvas.create_rectangle(x * self.gelazka_tamaina, y * self.gelazka_tamaina,
                                     (x + 1) * self.gelazka_tamaina, (y + 1) * self.gelazka_tamaina, fill=color)
    def tableroa_ezabatu(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, self.tamaina[0] * self.gelazka_tamaina,
                                     self.tamaina[1] * self.gelazka_tamaina, fill='#eee')

    def marraztu_tableroa(self):
        self.tableroa_ezabatu()
        for i in range(self.tab.tamaina[1]):
            for j in range(self.tab.tamaina[0]):
                if self.tab.tab[i][j]:
                    self.marratu_gelazka(j, i, self.tab.tab[i][j])
        if self.tab.pieza:
            for i in range(4):
                x = self.tab.posizioa[0] + self.tab.pieza.get_x(i)
                y = self.tab.posizioa[1] + self.tab.pieza.get_y(i)
                self.marratu_gelazka(y, x, self.tab.pieza.get_kolorea())
                self.marratu_gelazka(y, x, self.tab.pieza.get_kolorea())
        self.puntuazioa_eguneratu()

    def pausu_bat(self):

        try:
            self.tab.betetako_lerroak_ezabatu()
            if self.zailtasuna==1:
                self.tab.mugitu_behera(1)
            elif self.zailtasuna==2:
                self.tab.mugitu_behera(2)
            else:
                self.tab.mugitu_behera(3)
        except Exception as error:
            try:
                self.tab.pieza_finkotu(self.tab.posizioa)
                pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
                self.tab.sartu_pieza(random.choice(pieza_posibleak)())
            except Exception as e:
                print("GAMEOVER")
                DatuBase.rankingPertsonalaKudeatu(self.erab,self.tab.puntuazioa,self.zailtasuna)

                if self.zailtasuna==1:
                    DatuBase.rankingErrazaKudeatu(self.erab,self.tab.puntuazioa)
                if self.zailtasuna==2:
                    DatuBase.rankingErtainaKudeatu(self.erab,self.tab.puntuazioa)
                if self.zailtasuna==3:
                    DatuBase.rankingZailaKudeatu(self.erab,self.tab.puntuazioa)
                DatuBase.rankingGlobalaKudeatu(self.erab,self.tab.puntuazioa)

                showinfo(title="GAMEOVER", message="PARTIDA AMAITU DA, PUNTUAZIOA:  " + str(self.tab.puntuazioa))
                self.button.configure(state=ACTIVE)
                self.gorde.configure(state=DISABLED)
                self.kargatu.configure(state=ACTIVE)

                self.egiaztatuSaria()
                self.tab.hasieratu_tableroa()
                pygame.mixer.music.stop()
                return
        self.after(400, self.pausu_bat)
        self.marraztu_tableroa()

    def puntuazioa_eguneratu(self):
        if self.puntuazio_panela:
            self.puntuazio_panela.set(f"Puntuazioa: {self.tab.puntuazioa}")

    def joku_kontrola(self, event):
        try:
            if event.keysym == 'Up':
                self.tab.biratu_pieza()
            if event.keysym == 'Down':
                self.tab.pieza_kokatu_behean()
            if event.keysym == 'Right':
                self.tab.mugitu_eskumara()
            if event.keysym == 'Left':
                self.tab.mugitu_ezkerrera()
        except Exception as error:
            pass
        finally:
            self.marraztu_tableroa()


    def jolastu(self):
        self.button.configure(state=DISABLED)
        self.kargatu.configure(state=DISABLED)

        Pieza.Laukikolorea(Kontroladorea().laukiaLortu(self.erab))
        Pieza.lIspiluKolorea(Kontroladorea().lispiluLortu(self.erab))
        Pieza.lKolorea(Kontroladorea().lLortu(self.erab))
        Pieza.zKolorea(Kontroladorea().zLortu(self.erab))
        Pieza.zIspiluKolorea(Kontroladorea().zispiluLortu(self.erab))
        Pieza.ilaraKolorea(Kontroladorea().ilaraLortu(self.erab))
        Pieza.tKolorea(Kontroladorea().tLortu(self.erab))

        if self.jokatzen:
            self.after_cancel(self.jokatzen)
        pygame.mixer.init()
        if Kontroladorea().musikaLortu(self.erab) != "default":
            pygame.mixer.init()
            if(Kontroladorea.musikaLortu(self, self.erab) == 'Soundtrack 1: Ballad of Godness'):
                pygame.mixer.music.load('BalladOfGoddness.mp3')
            elif(Kontroladorea.musikaLortu(self,self.erab) == 'Soundtrack 2: Came And Get Your Love'):
                pygame.mixer.music.load('ComeAndGetYourLove.mp3')
            elif(Kontroladorea.musikaLortu(self,self.erab) == 'Soundtrack 3: Inazuma'):
                pygame.mixer.music.load('Inazuma.mp3')
            elif(Kontroladorea.musikaLortu(self,self.erab) == 'Soundtrack 4: Platino'):
                pygame.mixer.music.load('Platino.mp3')
            elif(Kontroladorea.musikaLortu(self,self.erab) == 'Soundtrack 5: Stars'):
                pygame.mixer.music.load('Stars.mp3')
            elif(Kontroladorea.musikaLortu(self,self.erab) == 'Soundtrack 6: Tetris remix'):
                pygame.mixer.music.load('TetrisRemix.mp3')
            pygame.mixer.music.play(-1)
        self.tab.hasieratu_tableroa()
        pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
        self.tab.sartu_pieza(random.choice(pieza_posibleak)())
        self.marraztu_tableroa()
        self.jokatzen = self.after(400, self.pausu_bat)

        self.gorde.configure(state=ACTIVE, command=lambda: Kontroladorea().gordePartida(self.tab))

    def lortuTableroa(self):

        self.tabBerria = Kontroladorea().kargatuPartida(self.zailtasuna, self.erab)
        if self.tabBerria is not None and self.tabBerria != -1:
            showinfo(title="ONDO", message="PARTIDA KARGATU DA")
            self.tab = self.tabBerria
            self.button.configure(state=DISABLED)

            Pieza.Laukikolorea(Kontroladorea().laukiaortu(self.erab))
            Pieza.lIspiluKolorea(Kontroladorea().lispiluLortu(self.erab))
            Pieza.lKolorea(Kontroladorea().lLortu(self.erab))
            Pieza.zKolorea(Kontroladorea().zLortu(self.erab))
            Pieza.zIspiluKolorea(Kontroladorea().zispiluLortu(self.erab))
            Pieza.ilaraKolorea(Kontroladorea().ilaraLortu(self.erab))
            Pieza.tKolorea(Kontroladorea().tLortu(self.erab))

            if self.jokatzen:
                self.after_cancel(self.jokatzen)

            pygame.mixer.init()
            if Kontroladorea().musikaLortu(self.erab) != "default":
                pygame.mixer.init()
                if (Kontroladorea.musikaLortu(self.erab) == 'Soundtrack 1: Ballad Of Goddness (TLOZ)'):
                    pygame.mixer.music.load('BalladOfGoddness.mp3')
                elif (Kontroladorea.musikaLortu(self.erab) == 'Soundtrack 2: Came And Get Your Love'):
                    pygame.mixer.music.load('ComeAndGetYourLove.mp3')
                elif (Kontroladorea.musikaLortu(self.erab) == 'Soundtrack 3: Inazuma'):
                    pygame.mixer.music.load('Inazuma.mp3')
                elif (Kontroladorea.musikaLortu(self.erab) == 'Soundtrack 4: Platino'):
                    pygame.mixer.music.load('Platino.mp3')
                elif (Kontroladorea.musikaLortu(self.erab) == 'Soundtrack 5: Stars'):
                    pygame.mixer.music.load('Stars.mp3')
                elif (Kontroladorea.musikaLortu(self.erab) == 'Soundtrack 6: Tetris remix'):
                    pygame.mixer.music.load('TetrisRemix.mp3')
                pygame.mixer.music.play(-1)

            pieza_posibleak = [Laukia, Zutabea, Lforma, LformaAlderantzizko, Zforma, ZformaAlderantzizko, Tforma]
            self.tab.sartu_pieza(random.choice(pieza_posibleak)())
            self.marraztu_tableroa()
            self.jokatzen = self.after(400, self.pausu_bat)

            self.gorde.configure(state=ACTIVE, command=lambda: Kontroladorea().gordePartida(self.tab))
            self.kargatu.configure(state=DISABLED)

    def egiaztatuSaria(self):

        datuak=Kontroladorea().sariakLortu(self.erab)
        erabil=datuak[0]
        irabaziErraz = datuak[1]
        irabaziErtain = datuak[2]
        irabaziZail = datuak[3]
        jarrai = datuak[4]
        erraza1 = datuak[5]
        erraza5 = datuak[6]
        erraza10 = datuak[7]
        ertaina1 = datuak[8]
        ertaina5 = datuak[9]
        ertaina10 = datuak[10]
        zaila1 = datuak[11]
        zaila5 = datuak[12]
        zaila10 = datuak[13]
        segidan = datuak[14]
        top = datuak[15]
        print (datuak)

        self.sariWindow=None
        img=None
        erra=False
        ert=False
        zla=False

        if self.tab.puntuazioa > 100: # 1000, para probar 100

            if self.zailtasuna == 1:
                za = "Erraza"
                erra = True
                irabaziErraz += 1
            elif self.zailtasuna == 2:
                za = "Ertaina"
                ert = True
                irabaziErtain += 1
            elif self.zailtasuna == 3:
                za = "Zaila"
                zla = True
                irabaziZail += 1

            jarrai+=1
            showinfo(title="Partida irabazi duzu!", message="Hau da zure jarraiko irabazi kopurua:" + str(jarrai))

            if (erra and erraza1 == 0 and irabaziErraz == 1) \
                    or (ert and ertaina1 == 0 and irabaziErtain == 1) \
                    or (zla and zaila1 == 0 and irabaziZail == 1)\
                    or (erra and erraza5 == 0 and irabaziErraz == 5) \
                    or (ert and ertaina5 == 0 and irabaziErtain == 5) \
                    or (zla and zaila5 == 0 and irabaziZail == 5) \
                    or (erra and erraza10 == 0 and irabaziErraz == 10) \
                    or (ert and ertaina10 == 0 and irabaziErtain == 10) \
                    or (zla and zaila10 == 0 and irabaziZail == 10):

                if erra:
                    showinfo(title= za + "_" + "PARTIDA" + str(irabaziErraz), message="Zorionak, zailtasun honetan saria lortu duzu")
                    if irabaziErraz==1:
                        erraza1=1
                        img = PhotoImage(file="./irudiak/sari1.png")
                    elif irabaziErraz==5:
                        erraza5=1
                        img = PhotoImage(file="./ISAD22_tetris/irudiak/sari5.png")

                    elif irabaziErraz==10:
                        erraza10=1
                        img = PhotoImage(file="./ISAD22_tetris/irudiak/sari10.png")

                elif ert:
                    showinfo(title= za + "_" + "PARTIDA" + str(irabaziErtain), message="Zorionak, zailtasun honetan saria lortu duzu")
                    if irabaziErtain==1:
                        ertaina1=1
                        img = PhotoImage(file="./irudiak/sari1.png")

                    elif irabaziErtain==5:
                        ertaina5=1
                        img = PhotoImage(file="./irudiak/sari5.png")

                    elif irabaziErtain==10:
                        ertaina10=1
                        img = PhotoImage(file="./irudiak/sari10.png")

                elif zla:
                    showinfo(title= za + "_" + "PARTIDA" + str(irabaziZail), message="Zorionak, zailtasun honetan saria lortu duzu")
                    if irabaziZail == 1:
                        zaila1 = 1
                        img = PhotoImage(file="./irudiak/sari1.png")

                    elif irabaziZail == 5:
                        zaila5 = 1
                        img = PhotoImage(file="./irudiak/sari5.png")

                    elif irabaziZail == 10:
                        zaila10 = 1
                        img = PhotoImage(file="./irudiak/sari10.png")

                self.tab.hasieratu_tableroa()
                self.sariWindow = tk.Toplevel()
                self.sariWindow.geometry('500x520')
                self.sariWindow.title("Zailtasun saria")


                fondoa = Label(self.sariWindow, image=img).place(x=0, y=0)

            if jarrai==3 and segidan==0:
                segidan=1
                showinfo(title="Segidan saria", message= "3 aldiz jarraian irabazteagatik, saria irabazi duzu")

                if self.tab.puntuazioa!=0:
                    self.tab.hasieratu_tableroa()
                if self.sariWindow==None:
                    self.sariWindow = tk.Toplevel()
                    self.sariWindow.geometry('500x520')
                self.sariWindow.title("Segidan saria")
                img = PhotoImage(file="./irudiak/sariSegidan.png")
                fondoa = Label(self.sariWindow, image=img).place(x=0, y=0)

            if top==0: #Kontroladorea().rankingeanDago(self.erab) and #hau da, ranking batean dago
                top=1
                showinfo(title="Ranking saria", message= "Ranking batean egoteagatik, saria irabazi duzu")

                if self.tab.puntuazioa != 0:
                    self.tab.hasieratu_tableroa()
                if self.sariWindow == None:
                    self.sariWindow = tk.Toplevel()
                    self.sariWindow.geometry('500x520')
                self.sariWindow.title("Ranking saria")
                img = PhotoImage(file="./irudiak/sariTop.png")
                fondoa = Label(self.sariWindow, image=img).place(x=0, y=0)



            #print(erabil, irabaziErraz, irabaziErtain, irabaziZail, jarrai, erraza1, erraza5, erraza10, ertaina1,ertaina5, ertaina10, zaila1, zaila5, zaila10, segidan, top)
            Kontroladorea().eguneratuSariak(erabil, irabaziErraz, irabaziErtain, irabaziZail, jarrai, erraza1, erraza5,
                                       erraza10, ertaina1, ertaina5, ertaina10, zaila1, zaila5, zaila10, segidan,
                                       top)
            if self.sariWindow!=None:
                self.sariWindow.mainloop()


        else: #galdu badu
            jarrai = 0
            #print(erabil, irabaziErraz, irabaziErtain, irabaziZail, jarrai, erraza1, erraza5, erraza10, ertaina1,ertaina5, ertaina10, zaila1, zaila5, zaila10, segidan, top)
            Kontroladorea().eguneratuSariak(erabil, irabaziErraz, irabaziErtain, irabaziZail, jarrai, erraza1, erraza5,
                                       erraza10, ertaina1, ertaina5, ertaina10, zaila1, zaila5, zaila10, segidan, top)

