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
	
		def multiply(first, second): # Multiplican para evirtar problemas de recursion
			return super().__mul__(second)
			
		def verifyZeros(num):	# Metodo que retorna True si en el vector solo tiene 0s
			for i in range(num.can):
				if(num.valor[-(i+1)]!=0):
					return False
			return True
			
		if(self.can == 1 or other.can == 1):	#Primer Caso base
			#print("aaaa caso raro")
			#print(self, other)
			#number = self.convertInt(self.valor)*self.convertInt(other.valor)
			#return Knumero(number)
			return super().__mul__(other)
		else:
			div = max(self.can, other.can)
			div2 = div//2
			#print(div,"div")
			Lself = self.valor[-self.can:]
			Lother = other.valor[-other.can:]
			#print(Lself, Lother, "Nuevo K")
			a = Knumero(0)
			a.setVector(Lself[:self.can//2])
			b = Knumero(0)
			b.setVector(Lself[self.can//2:])
			c = Knumero(0)
			c.setVector(Lother[:other.can//2])
			d = Knumero(0)
			d.setVector(Lother[other.can//2:])
			#print(a,b,c,d, "'''''''''''''''")
			
			#-----------Verificacion si al dividir los knum uno sale con solo 0s
			if(verifyZeros(a)) or verifyZeros(b) or verifyZeros(c) or verifyZeros(d):
				#number = self.convertInt(self.valor)*self.convertInt(other.valor)
				#return Knumero(number)
				return super().__mul__(other)
			
			#----------
			
			#print(div)
			b1 = Knumero(10**div)
			b2 = Knumero(10**(div//2))
			#print("b1 ", b1)
			#print("b2 ", b2)
			#print(a, b, c, d ,"abcd")
			z2 = a*c
			
			#print(z2,"z2")
			#print(b, d,"b*d")
			z0 = b*d
			#print(z0,"z0")
			
			z1 = ((a+b)*(c+d)-z2)-z0
			
			#print(z1, "z1")
			#print("-------------------", z2, z1, z0)
			res = (z2*b1)+(z1*b2)+z0
			#print(res, "ardillita")
			return  res
		"""
		def magic(v1, v2, c1, c2):
			if(c1 < 3 and c2 < 3):
				#multiplicacion...
			else:
		return magic(self.valor, other.valor)
		"""