"""
	Autores: Joy Bonilla, Oscar Arroyo, Natalia Solano, Jose Pablo Perez - 8AM
"""
from Numero import *

class Knumero(Numero):
	def __init__(self, num):
		super().__init__(num)

	def setVector(self, vec):
		self.valor = [0]*self.size
		self.can=0
		for i in range(len(vec)):
			self.valor[-(i+1)]=vec[-(i+1)]
			self.can +=1
	

		
	def __mul__(self, other):
		if(self.can == 1 or other.can == 1):
			print(self.valor, other.valor, "aaaaa")
			a1 = self.convertInt(self.valor[-self.can:])
			b1 = self.convertInt(other.valor[-other.can:])
			print(self.can, other.can, "can")
			print(b1)
			num = a1 * b1
			aux = Knumero(num)
			print(aux, "aux")
			return aux
		else:
			div = max(self.can, other.can)
			print(div,"div")
			Lself = self.valor[-self.can:]
			Lother = other.valor[-other.can:]
			print(Lself, Lother, "lll")
			a = Knumero(0)
			a.setVector(Lself[:self.can//2])
			#print(a,"a")
			b = Knumero(0)
			b.setVector(Lself[self.can//2:])

			c = Knumero(0)
			c.setVector(Lother[:other.can//2])
			d = Knumero(0)
			d.setVector(Lother[other.can//2:])
			b1 = Knumero(10**self.can)
			b2 = Knumero(10**(self.can//2))
			print(a, c,"a*c")
			z2 = a*c
			print(z2,"z2")
			print(b, d,"b*d")
			z0 = b*d
			print(z0,"z0")
			z1 = (a+b)*(c+d)-z2-z0
			print(z1, "z1")
			
			return  (z2>>b1)+z1*b2+z0
		"""
		def magic(v1, v2, c1, c2):
			if(c1 < 3 and c2 < 3):
				#multiplicacion...
			else:
		return magic(self.valor, other.valor)
		"""