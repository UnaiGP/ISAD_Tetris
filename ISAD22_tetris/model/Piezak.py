from view import JokatuLeioa
from model.DatuBase import *
from view.JokatuLeioa import *


class Pieza:
	def __init__(self, forma, kolorea,mota):
		self.forma = forma
		self.kolorea = kolorea
		self.mota=mota
		self.erabiltzailea="null"




	def Laukikolorea(kol):
		global LaukiKolorea
		LaukiKolorea = kol
		return LaukiKolorea
	def ilaraKolorea(kol):
		global ilaraKolorea
		ilaraKolorea=kol
		return ilaraKolorea
	def lKolorea(kol):
		global lKolorea
		lKolorea=kol
		return lKolorea
	def lIspiluKolorea(kol):
		global lIspiluKolorea
		lIspiluKolorea=kol
		return lIspiluKolorea
	def zKolorea(kol):
		global zKolorea
		zKolorea=kol
		return zKolorea
	def zIspiluKolorea(kol):
		global zIspiluKolorea
		zIspiluKolorea=kol
		return zIspiluKolorea
	def tKolorea(kol):
		global tKolorea
		tKolorea=kol
		return tKolorea
	def get_kolorea(self):
		return self.kolorea

	def get_x(self, i):
		return self.forma[i][0]
	def get_y(self, i):
		return self.forma[i][1]

	def set_x(self, i,b):
		self.forma[i][0] = b
	def set_y(self, i,b):
		self.forma[i][1] = b

	def biratuEzkerrera(self):
		for i in range(4):
			aurr_x = self.get_x(i)
			aurr_y = self.get_y(i)
			self.set_x(i, aurr_y)
			self.set_y(i, -aurr_x)

	def biratuEskuinera(self):
		for i in range(4):
			aurr_x = self.get_x(i)
			aurr_y = self.get_y(i)
			self.set_x(i, -aurr_y)
			self.set_y(i, aurr_x)


	def min_x(self):
		return min([x[0] for x in self.forma])
	def min_y(self):
		return min([x[1] for x in self.forma])

class Laukia(Pieza):
	def __init__(self, kolorea=None,mota=None):

		super(Laukia, self).__init__([[0,0],[0,1],[1,0],[1,1]], kolorea=LaukiKolorea,mota="laukia")

class Zutabea(Pieza):
	def __init__(self, kolorea=None,mota=None):
		super(Zutabea, self).__init__([[0,-1],[0,0],[0,1],[0,2]], kolorea=ilaraKolorea,mota="ilara")

class Lforma(Pieza):
	def __init__(self, kolorea=None,mota=None):
		super(Lforma, self).__init__([[-1,-1],[0,-1],[0,0],[0,1]], kolorea=lKolorea,mota="l")

class LformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None,mota=None):
		super(LformaAlderantzizko, self).__init__([[1,-1],[0,-1],[0,0],[0,1]], kolorea=lIspiluKolorea,mota="l ispilu")

class Zforma(Pieza):
	def __init__(self, kolorea=None,mota=None):
		super(Zforma, self).__init__([[0,-1],[0,0],[-1,0],[-1,1]], kolorea=zKolorea,mota="z")

class ZformaAlderantzizko(Pieza):
	def __init__(self, kolorea=None,mota=None):

		super(ZformaAlderantzizko, self).__init__([[0,-1],[0,0],[1,0],[1,1]], kolorea=zIspiluKolorea,mota="z ispilu")

class Tforma(Pieza):
	def __init__(self, kolorea=None,mota=None):
		super(Tforma, self).__init__([[-1,0],[0,0],[1,0],[0,1]], kolorea=tKolorea,mota="T")