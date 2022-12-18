import sqlite3
from os import path
import pickle

from tkinter import *
from tkinter.messagebox import showinfo, showerror


class DatuBase(object):
    def __init__(self):
        super(DatuBase, self).__init__()

        if not path.exists("datubasea.db"):
            db = sqlite3.connect("datubasea.db")
            c = db.cursor()

            #c.execute("DROP TABLE erabiltzaileak")

            c.execute(
                "CREATE TABLE erabiltzaileak('erab','ps','background','soinua','lauki','ilara','l','lispilu','z','zispilu','t')")

            c.execute("CREATE TABLE sariak('erab','irabaziErraz' NUMERIC,'irabaziErtain' NUMERIC,'irabaziZail' NUMERIC ,'irabaziJarrai' NUMERIC ,'erraza1' NUMERIC ,'erraza5' NUMERIC ,'erraza10' NUMERIC,'ertaina1' NUMERIC ,'ertaina5' NUMERIC ,'ertaina10' NUMERIC,'zaila1' NUMERIC ,'zaila5' NUMERIC,'zaila10' NUMERIC, 'segidan' NUMERIC ,'top' NUMERIC)")

            c.execute("CREATE TABLE rankingPertsonal('erab','punt1','punt2','punt3','punt4','punt5','punt6','punt7','punt8','punt9','punt10')")

            # c.execute( "CREATE TABLE erabiltzaileak('erab','ps','background','soinua','lauki','ilara','l','lispilu','z','zispilu','t')")
            #c.execute("DROP TABLE rankingGlobal")
            #c.execute("DROP TABLE rankingErraza")
            #c.execute("DROP TABLE rankingErtaina")
            #c.execute("DROP TABLE rankingZaila")
            c.execute("DROP TABLE rankingGlobal")
            c.execute("DROP TABLE rankingErraza")
            c.execute("DROP TABLE rankingErtaina")
            c.execute("DROP TABLE rankingZaila")
            c.execute(
                "CREATE TABLE rankingGlobal('erab','punt1')")
            c.execute(
                "CREATE TABLE rankingErraza('erab','punt1')")
            c.execute(
                "CREATE TABLE rankingErtaina('erab','punt1')")
            c.execute(
                "CREATE TABLE rankingZaila('erab','punt1')")

            c.close()


    def saioHasi(self, erabiltzailea, pasahitza):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        erabiltzaile = erabiltzailea
        pasahitz = pasahitza
        i=0
        res = c.execute("SELECT * FROM erabiltzaileak WHERE erab=? AND ps=?", (erabiltzaile, pasahitz))
        if res.fetchall():
            showinfo(title="SAIOA ONDO HASITA", message="Erabiltzaile eta pasahitza zuzenak")



            return True
        else:
            showerror(title="SAIOA EZIN DA HASI", message="Erabiltzaile edo pasahitza gaizki")
            return False
        c.close()

    def erregistroa(self, erabiltzailea, pasahitza):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        erabiltzaile = erabiltzailea
        pasahitz = pasahitza
        i=0
        res = c.execute("SELECT * FROM erabiltzaileak WHERE erab=?", [erabiltzaile])
        if len(res.fetchall()) == 0:
            c.execute("INSERT INTO erabiltzaileak VALUES (?, ?,?,?,?,?,?,?,?,?,?)", (erabiltzaile, pasahitz, "red", "default", "cyan", "brown", "blue", "purple", "white", "red", "pink"))
            c.execute("INSERT INTO sariak VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(erabiltzaile, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0))
            c.execute("INSERT INTO rankingPertsonal VALUES(?,?,?,?,?,?,?,?,?,?,?)",(erabiltzaile,0,0,0,0,0,0,0,0,0,0))


            showinfo(title="ERREGISTROA EGINDA", message="Erabiltzaile eta pasahitza zuzenak")
            con.commit()
            return True
        else:
            showerror(title="ERREGISTROA EZIN DA EGIN", message="Erabiltzailearen izena erabilita dago jada")
            return False

        c.close()

    def rankingPertsonalaKudeatu(izena, puntuazioa, zailtasuna):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()

        res = c.execute("SELECT * FROM rankingPertsonal where erab=?", [izena])
        datua = DatuBase.LortuP(res)
        print(datua)
        if puntuazioa > datua[0]:
            datua[0] = puntuazioa
            datua.sort()
            c.execute("UPDATE rankingPertsonal SET punt1=? WHERE erab=?", [datua[0], izena])
            c.execute("UPDATE rankingPertsonal SET punt2=? WHERE erab=?", [datua[1], izena])
            c.execute("UPDATE rankingPertsonal SET punt3=? WHERE erab=?", [datua[2], izena])
            c.execute("UPDATE rankingPertsonal SET punt4=? WHERE erab=?", [datua[3], izena])
            c.execute("UPDATE rankingPertsonal SET punt5=? WHERE erab=?", [datua[4], izena])
            c.execute("UPDATE rankingPertsonal SET punt6=? WHERE erab=?", [datua[5], izena])
            c.execute("UPDATE rankingPertsonal SET punt7=? WHERE erab=?", [datua[6], izena])
            c.execute("UPDATE rankingPertsonal SET punt8=? WHERE erab=?", [datua[7], izena])
            c.execute("UPDATE rankingPertsonal SET punt9=? WHERE erab=?", [datua[8], izena])
            c.execute("UPDATE rankingPertsonal SET punt10=? WHERE erab=?", [datua[9], izena])

        ex = c.execute("SELECT * FROM rankingPertsonal where erab=?", [izena])
        emaitza = DatuBase.LortuP(ex)
        con.commit()
        c.close()

    def pasahitzaBerreskuratu(self,izenaEntry):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        erabil = izenaEntry
        res = c.execute("SELECT ps FROM erabiltzaileak WHERE erab=?", [erabil])
        if res.fetchall():
            res2 = c.execute("SELECT ps FROM erabiltzaileak WHERE erab=?", [erabil])
            datua = self.pasahitzaLortu(res2)
            showinfo(title="PASAHITZA BERRESKURATUTA", message="Hau da zure pasahitza: " +"(" + datua + ")")
        else:
            showerror(title="PASAHITZA EZ DA BERRESKURATU", message="Ezin da posible izan pasahitza berreskuratzea")
        c.close()

    def LortuP(res):
        lista = []
        i = 1
        for row in res:
            if row is not None:
                while i < len(row):
                    datua = (row[i])
                    lista.append(datua)
                    i = i + 1
        return lista
    def Lortu(res):
        lista = []
        i = 0
        for row in res:
            if row is not None:
                while i==0:
                    datua = (row[i])
                    lista.append(datua)
                    i=1
        return lista
    def zenbatRanking(self,mota):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        array=[]
        kont=0;
        if mota==globala:
            res=c.execute((""))

    def pasahitzaLortu(self, res):
        for row in res:
            if row is not None:
                datua = str(row[0])
                return datua
    def setSoinua(self, erab,option):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        c.execute("UPDATE erabiltzaileak SET soinua=? WHERE erab=?", [option, erab])
        con.commit()
        c.close
    def setBackground(self, erab, option):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        c.execute("UPDATE erabiltzaileak SET background=? WHERE erab=?", [option, erab])
        con.commit()
        c.close
    def setLauki(self, erab,option):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res=c.execute("UPDATE erabiltzaileak SET lauki=? WHERE erab=?",[option,erab])
        con.commit()
        c.close
    def setIlara(self, erab,option):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res=c.execute("UPDATE erabiltzaileak SET ilara=? WHERE erab=?",[option,erab])
        con.commit()
        c.close
    def setL(self, erab,option):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res=c.execute("UPDATE erabiltzaileak SET l=? WHERE erab=?",[option,erab])
        con.commit()
        c.close
    def setSLispilu(self, erab,option):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res=c.execute("UPDATE erabiltzaileak SET lispilu=? WHERE erab=?",[option,erab])
        con.commit()
        c.close
    def setZ(self, erab,option):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res=c.execute("UPDATE erabiltzaileak SET z=? WHERE erab=?",[option,erab])
        con.commit()
        c.close

    def setZispilu(self, erab, option):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("UPDATE erabiltzaileak SET zispilu=? WHERE erab=?", [option, erab])
        con.commit()
        c.close

    def setT(self, erab, option):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("UPDATE erabiltzaileak SET t=? WHERE erab=?", [option, erab])
        con.commit()
        c.close
    def musikaLortu(self,erab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res=c.execute("SELECT soinua FROM erabiltzaileak WHERE erab=?",[erab])
        if res.fetchall():
            res2=c.execute("SELECT soinua FROM erabiltzaileak WHERE erab=?",[erab])
            for row in res2:
                if row is not None:
                    datua=str(row[0])
                    return datua
        c.close()

    def backgroundLortu(self, erab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT background FROM erabiltzaileak WHERE erab=?", [erab])
        if res.fetchall():
            res2 = c.execute("SELECT background FROM erabiltzaileak WHERE erab=?", [erab])
            for row in res2:
                if row is not None:
                    datua = str(row[0])
                    return datua
        c.close()

    def ilaraLortu(self, erab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT ilara FROM erabiltzaileak WHERE erab=?", [erab])
        if res.fetchall():
            res2 = c.execute("SELECT ilara FROM erabiltzaileak WHERE erab=?", [erab])
            for row in res2:
                if row is not None:
                    datua = str(row[0])
                    return datua
        c.close()

    def laukiaLortu(self, erab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT lauki FROM erabiltzaileak WHERE erab=?", [erab])
        if res.fetchall():
            res2 = c.execute("SELECT lauki FROM erabiltzaileak WHERE erab=?", [erab])
            for row in res2:
                if row is not None:
                    datua = str(row[0])
                    return datua
        c.close()

    def lLortu(self, erab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT l FROM erabiltzaileak WHERE erab=?", [erab])
        if res.fetchall():
            res2 = c.execute("SELECT l FROM erabiltzaileak WHERE erab=?", [erab])
            for row in res2:
                if row is not None:
                    datua = str(row[0])
                    return datua
        c.close()

    def lispiluLortu(self, erab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT lispilu FROM erabiltzaileak WHERE erab=?", [erab])
        if res.fetchall():
            res2 = c.execute("SELECT lispilu FROM erabiltzaileak WHERE erab=?", [erab])
            for row in res2:
                if row is not None:
                    datua = str(row[0])
                    return datua
        c.close()

    def zLortu(self, erab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT z FROM erabiltzaileak WHERE erab=?", [erab])
        if res.fetchall():
            res2 = c.execute("SELECT z FROM erabiltzaileak WHERE erab=?", [erab])
            for row in res2:
                if row is not None:
                    datua = str(row[0])
                    return datua
        c.close()

    def zispiluLortu(self, erab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT zispilu FROM erabiltzaileak WHERE erab=?", [erab])
        if res.fetchall():
            res2 = c.execute("SELECT zispilu FROM erabiltzaileak WHERE erab=?", [erab])
            for row in res2:
                if row is not None:
                    datua = str(row[0])
                    return datua
        c.close()

    def tLortu(self, erab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT t FROM erabiltzaileak WHERE erab=?", [erab])
        if res.fetchall():
            res2 = c.execute("SELECT t FROM erabiltzaileak WHERE erab=?", [erab])
            for row in res2:
                if row is not None:
                    datua = str(row[0])
                    return datua
        c.close()
    def erabiltzaileaEzabatu(self, ezabatzekoErab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        aurkitua = False
        res = c.execute("SELECT * FROM erabiltzaileak")
        for row in res:
            if row is not None:
                erab = str(row[0])
                ps = str(row[1])
                if (ezabatzekoErab == erab):
                    aurkitua = True
                    showinfo(title="EZABATZEKO ERABILTZAILEA",
                             message="Hau da ezabatuko den erabiltzailea: " + "(" + erab + ")" + " eta bere pasahitza:" + "(" + ps + ")")
                    c.execute("DELETE FROM erabiltzaileak WHERE erab= ?", (erab,))
                    con.commit()
                    showinfo(title="ONDO", message="Erabiltzailearen datuak ezabatu dira")
        if aurkitua == False:
            showerror(title="EZ DA AURKITU ERABILTZAILEA", message="Ez da ezer ezabatuko")


    def erabiltzaileakPrintatuAdmin(self):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT * FROM erabiltzaileak")
        return res

    def erabiltzaieakPrintatu(self, punt):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()

        res = c.execute("SELECT erab FROM rankingErraza WHERE punt1=?", [punt]).fetchall()
        if len(res)==0:
            res = c.execute("SELECT erab FROM rankingErtaina WHERE punt1=?", [punt]).fetchall()
            if len(res)==0:
                res = c.execute("SELECT erab FROM rankingZaila WHERE punt1=?", [punt]).fetchall()

        return res[0]
        c.close()

    def erabiltzaieakPrinteatuErraza(self, punt):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT erab FROM rankingErraza WHERE punt1=?", [punt]).fetchall()
        return res[0]

        c.close()

    def erabiltzaieakPrinteatuErtaina(self, punt):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT erab FROM rankingErtaina WHERE punt1=?", [punt]).fetchall()
        return res[0]
        c.close()

    def erabiltzaieakPrinteatuZaila(self, punt):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT erab FROM rankingZaila WHERE punt1=?", [punt]).fetchall()
        return res[0]
        c.close()

    def rankingPrintatu(self, mota, erab):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()


        if(mota == 2):
            res = c.execute("SELECT * FROM rankingPertsonal WHERE erab= ?", [erab])
            res=DatuBase.LortuP(res)

            res.sort()
        elif (mota==3):
            res=c.execute("SELECT punt1 FROM rankingGlobal ")
            res=res.fetchall()

        elif (mota==4):
            res = c.execute("SELECT punt1 FROM rankingErraza ")
            res = res.fetchall()

        elif (mota==5):
            res = c.execute("SELECT punt1 FROM rankingErtaina ")
            res = res.fetchall()

        elif (mota==6):
            res = c.execute("SELECT punt1 FROM rankingZaila ")
            res = res.fetchall()


        return res
    def erabiltzaileKop(self):
        kont=0
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT * FROM erabiltzaileak")
        for row in res:
            if row is not None:
                kont= kont +1
        return kont

    def rankingErrazaKudeatu(izena,puntuazioa):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT punt1 FROM rankingErraza")

        datua = res.fetchall()
        i = 0

        res1 = datua
        while i < len(datua):
            a = str(res1[i])
            hitza = (a.translate({ord(','): None}))
            hitza = (hitza.translate({ord('('): None}))
            hitza = (hitza.translate({ord(')'): None}))
            hitza = hitza.replace("'", "")
            datua[i] = int(float(hitza))
            i = i + 1

        datua.sort(key=int)

        if puntuazioa > datua[0]:

            c.execute("UPDATE rankingErraza SET erab=? WHERE punt1=?", (izena, (datua[0])))
            c.execute("UPDATE rankingErraza SET punt1=? WHERE punt1=?", (puntuazioa, (datua[0])))

            con.commit()
            c.close()

    def rankingErtainaKudeatu(izena,puntuazioa):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT punt1 FROM rankingErtaina")

        datua = res.fetchall()
        i = 0

        res1 = datua
        while i < len(datua):
            a = str(res1[i])
            hitza = (a.translate({ord(','): None}))
            hitza = (hitza.translate({ord('('): None}))
            hitza = (hitza.translate({ord(')'): None}))
            hitza = hitza.replace("'", "")
            datua[i] = int(float(hitza))
            i = i + 1

        datua.sort(key=int)

        if puntuazioa > datua[0]:
            c.execute("UPDATE rankingErtaina SET erab=? WHERE punt1=?", (izena, (datua[0])))
            c.execute("UPDATE rankingErtaina SET punt1=? WHERE punt1=?", (puntuazioa, (datua[0])))

            con.commit()
            c.close()
    def rankingZailaKudeatu(izena,puntuazioa):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT punt1 FROM rankingZaila")

        datua = res.fetchall()
        i=0


        res1 = datua
        while i < len(datua):
            a = str(res1[i])
            hitza = (a.translate({ord(','): None}))
            hitza = (hitza.translate({ord('('): None}))
            hitza = (hitza.translate({ord(')'): None}))
            hitza = hitza.replace("'", "")
            datua[i] = int(float(hitza))
            i = i + 1

        datua.sort(key=int)


        if puntuazioa > datua[0]:
            c.execute("UPDATE rankingZaila SET erab=? WHERE punt1=?", (izena, (datua[0])))
            c.execute("UPDATE rankingZaila SET punt1=? WHERE punt1=?", (puntuazioa, (datua[0])))

            con.commit()
            c.close()





    def rankingGlobalaKudeatu(izena,puntuazioa):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT punt1 FROM rankingGlobal")
        print(izena)
        datua = res.fetchall()
        i = 0

        res1 = datua
        while i < len(datua):
            a = str(res1[i])
            hitza = (a.translate({ord(','): None}))
            hitza = (hitza.translate({ord('('): None}))
            hitza = (hitza.translate({ord(')'): None}))
            hitza = hitza.replace("'", "")
            datua[i] = int(float(hitza))
            i = i + 1

        datua.sort(key=int)
        print(datua)
        if puntuazioa > datua[0]:
            c.execute("UPDATE rankingGlobal SET erab=? WHERE punt1=?", (izena, (datua[0])))
            c.execute("UPDATE rankingGlobal SET punt1=? WHERE punt1=?", (puntuazioa, (datua[0])))
            con.commit()
            c.close()


    def aldatuPasahitza(self, erab, pas, berria):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        erabil = erab
        res = c.execute("SELECT ps FROM erabiltzaileak WHERE erab=?", [erabil])
        if res.fetchall():
            res2 = c.execute("SELECT ps FROM erabiltzaileak WHERE erab=?", [erabil])
            pasahitza = self.pasahitzaLortu(res2)
            if(pasahitza == pas):
                c.execute("UPDATE erabiltzaileak SET ps=? WHERE erab=?", (berria, erab))
                con.commit()
                showinfo(title="PASAHITZA ALDATUA", message="Pasahitza aldatu da")
                return True
            else:
                showinfo(title="PASAHITZA OKERRA", message="Pasahitza okerra da")
                return False
        else:
            showerror(title="PASAHITZA EZ DA ALDATU", message="Erabiltzailea ez da existitzen")
            return False
        c.close()



    def gordePartida(self,tab,erab):

        if tab.zailtasun == 1:
            errazaGorde = tab
            artxiboBinario=open("errazaGorde" + "_" + erab,"wb")
            pickle.dump(errazaGorde,artxiboBinario)
            artxiboBinario.close()
            showinfo(title="ONDO", message=" ERRAZA ZAILTASUNEKO PARTIDA GORDE DA")

        elif tab.zailtasun == 2:
            ertainaGorde = tab
            artxiboBinario = open("ertainaGorde" + "_" + erab, "wb")
            pickle.dump(ertainaGorde, artxiboBinario)
            artxiboBinario.close()
            showinfo(title="ONDO", message=" ERTAINA ZAILTASUNEKO PARTIDA GORDE DA")

        elif tab.zailtasun == 3:
            zailaGorde = tab
            artxiboBinario = open("zailaGorde" + "_" + erab, "wb")
            pickle.dump(zailaGorde, artxiboBinario)
            artxiboBinario.close()
            showinfo(title="ONDO", message=" ZAILA ZAILTASUNEKO PARTIDA GORDE DA")


        if (tab.zailtasun ==1 and not path.exists("errazaGorde")) or (tab.zailtasun==2 and not path.exists("ertainaGorde")) or (tab.zailtasun==3 and not path.exists("zailaGorde")):
            return -1



    def kargatuPartida(self,zailtasuna,erab):
        if zailtasuna == 1:

            if path.exists("errazaGorde" + "_" + erab):
                artxibo=open("errazaGorde" + "_" + erab, "rb")
                tabGordeta=pickle.load(artxibo)
                return tabGordeta

            else:
                showerror(title="GAIZKI", message="EZ DAUDE ERRAZA MOTAKO GORDETAKO PARTIDARIK")
                return -1

        elif zailtasuna == 2:

            if path.exists("ertainaGorde" + "_" + erab):
                artxibo = open("ertainaGorde" + "_" + erab, "rb")
                tabGordeta = pickle.load(artxibo)
                return tabGordeta

            else:
                showerror(title="GAIZKI", message="EZ DAUDE ERTAINA MOTAKO GORDETAKO PARTIDARIK")
                return -1

        elif zailtasuna == 3:

            if path.exists("zailaGorde" + "_" + erab):
                artxibo = open("zailaGorde" + "_" + erab, "rb")
                tabGordeta = pickle.load(artxibo)
                return tabGordeta

            else:
                showerror(title="GAIZKI", message="EZ DAUDE ZAILA MOTAKO GORDETAKO PARTIDARIK")
                return -1

    def sariakLortu(self,erab):

        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        erabil = erab
        res = c.execute("SELECT * FROM sariak WHERE erab=?", [erabil])
        if res.fetchall():
            res2 = c.execute("SELECT * FROM sariak WHERE erab=?", [erabil])
            for row in res2:
                if row is not None:
                    datuak = row
                    return datuak
        c.close()

    def eguneratuSariak(self,erabil,irabaziErraz, irabaziErtain, irabaziZail,jarrai,erraza1,erraza5,erraza10,ertaina1,ertaina5,ertaina10,zaila1,zaila5,zaila10,segidan,top):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        c.execute("UPDATE sariak SET irabaziErraz= ? , irabaziErtain= ? , irabaziZail= ?, "
                  "irabaziJarrai=? , erraza1= ? , "
                  "erraza5= ? , erraza10= ? , ertaina1= ? , ertaina5= ? , ertaina10= ? , "
                  "zaila1= ? , zaila5= ? , zaila10= ? , segidan= ? , top= ?  "
                  " WHERE erab=?", (irabaziErraz,irabaziErtain,irabaziZail,jarrai,erraza1,erraza5,erraza10,ertaina1,ertaina5,ertaina10,zaila1,zaila5,zaila10,segidan,top, erabil))
        con.commit()
        c.close()


    def rankingeanDago(self,erabil):
        con = sqlite3.connect("datubasea.db")
        c = con.cursor()
        res = c.execute("SELECT erab FROM ranking WHERE erab=? ", [erabil])
        if res.fetchall():
            return True
        else:
            return False
        c.close()



