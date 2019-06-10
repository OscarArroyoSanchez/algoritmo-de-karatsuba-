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
			
	def __repr__(self):
		aux = 0
		for i in range(self.can):
			aux+=self.valor[-(i+1)]*self.base**i
		return f"Knumero({aux})"

		
	def __mul__(self, other):

		def verifyZeros(num):	# Metodo que retorna True si en el vector solo tiene 0s
			for i in range(num.can):
				if(num.valor[-(i+1)]!=0):
					return False
			return True
		if(self.can//2>=other.can or other.can//2>=self.can):
			number = self.convertInt(self.valor)*self.convertInt(other.valor)
			return Knumero(number)
		if(self.can == 1 or other.can == 1):	#Primer Caso base

			number = self.convertInt(self.valor)*self.convertInt(other.valor)
			return Knumero(number)

		else:
			div = max(self.can, other.can)

			div2 = div//2

			Lself = self.valor[-self.can:]
			Lother = other.valor[-other.can:]

			a = Knumero(0)
			a.setVector(Lself[:self.can//2])
			b = Knumero(0)
			b.setVector(Lself[self.can//2:])
			c = Knumero(0)
			c.setVector(Lother[:other.can//2])
			d = Knumero(0)
			d.setVector(Lother[other.can//2:])

			
			#-----------Verificacion si al dividir los knum uno sale con solo 0s
			if(verifyZeros(a)) or verifyZeros(b) or verifyZeros(c) or verifyZeros(d):
				return super().__mul__(other)
			
			#----------
			
			b1 = Knumero(self.base**(div))
			b2 = Knumero(self.base**(div//2))
			b3 = Knumero(self.base**(div//4))

			z2 = a*c

			z0 = b*d
			
			z1 = (a+b)*(c+d)-z2-z0

			(z2*b1)+(z1*b2)+z0
			
			return  
		"""
		def magic(v1, v2, c1, c2):
			if(c1 < 3 and c2 < 3):
				#multiplicacion...
			else:
		return magic(self.valor, other.valor)
		"""