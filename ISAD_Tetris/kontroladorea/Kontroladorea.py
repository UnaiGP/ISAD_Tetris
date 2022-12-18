import view
from model.DatuBase import *

class Kontroladorea(object):
    def __init__(self):
        super(Kontroladorea, self).__init__()


    #SaioHasiera
    def saioHasi(self,erab,pas):
        return DatuBase().saioHasi(erab,pas)

    #Erregistroa
    def erregistroa(self,erab,pas):
        return DatuBase().erregistroa(erab, pas)

    #Admin Leihoa
    def erabiltzaileaEzabatu(self,erab):
        DatuBase().erabiltzaileaEzabatu(erab)


    def erabiltzaileakPrintatuAdmin(self):
        return DatuBase().erabiltzaileakPrintatuAdmin()

    def erabiltzaileakPrintatu(self,punt):
        return DatuBase().erabiltzaileakPrintatu(punt)

    #jokatu Leihoa
    def musikaLortu(self,erab):
        return DatuBase().musikaLortu(erab)

    def backgroundLortu(self,erab):
        return DatuBase().backgroundLortu(erab)

    def laukiaLortu(self,erab):
        return DatuBase().laukiaLortu(erab)

    def lispiluLortu(self,erab):
        return DatuBase().lispiluLortu(erab)

    def lLortu(self,erab):
        return DatuBase().lLortu(erab)

    def zLortu(self,erab):
        return DatuBase().zLortu(erab)

    def zispiluLortu(self,erab):
        return DatuBase().zispiluLortu(erab)

    def ilaraLortu(self,erab):
        return DatuBase().ilaraLortu(erab)

    def tLortu(self,erab):
        return DatuBase().tLortu(erab)

    def gordePartida(self,tab,erab):
        return DatuBase().gordePartida(tab, erab)

    def kargatuPartida(self,zailtasuna,erab):
        return DatuBase().kargatuPartida(zailtasuna,erab)

    def sariakLortu(self,erab):
        return DatuBase().sariakLortu(erab)

    def rankingeanDago(self,erab):
        return DatuBase().rankingeanDago(erab)

    def eguneratuSariak(self, erabil, irabaziErraz, irabaziErtain, irabaziZail, jarrai, erraza1, erraza5, erraza10,
                        ertaina1, ertaina5, ertaina10, zaila1, zaila5, zaila10, segidan, top):
        DatuBase().eguneratuSariak(erabil, irabaziErraz, irabaziErtain, irabaziZail, jarrai, erraza1, erraza5,
                                   erraza10, ertaina1, ertaina5, ertaina10, zaila1, zaila5, zaila10, segidan,
                                   top)

    #PasahitzaAldatu

    def aldatuPasahitza(self,erab,pas,berria):
        return DatuBase().aldatuPasahitza(erab,pas,berria)

    #PasahitzBerreskurapena

    def pasahitzaBerreskuratu(self, erab):
        DatuBase().pasahitzaBerreskuratu(erab)

    #PertsonalizazioLeihoa

    def setBackground(self,erab,option):
        DatuBase().setBackground(erab, option)

    def setSoinua(self,erab,option):
        DatuBase().setSoinua(erab, option)

    def setLauki(self,erab,option):
        DatuBase().setLauki(erab, option)

    def setIlara(self,erab,option):
        DatuBase().setIlara(erab, option)

    def setL(self,erab,option):
        DatuBase().setL(erab, option)

    def setSLispilu(self,erab,option):
        DatuBase().setSLispilu(erab, option)

    def setZ(self,erab,option):
        DatuBase().setZ(erab, option)

    def setZispilu(self,erab,option):
        DatuBase().setZispilu(erab, option)

    def setT(self,erab,option):
        DatuBase().setT(erab, option)
