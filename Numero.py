"""
	Autores: Joy Bonilla, Oscar Arroyo, Natalia Solano, Jose Pablo Perez - 8AM
"""
from NumSpecs import *

@total_ordering
class Numero(NumSpecs):
	def __init__(self, num = 0, tam = 16, base = 10):
		super().__init__(tam)
		self.valor = [0] * tam
		self.base = base
		self.can = 0
		if(num > 0):
			for i in range (tam):			#Guarda num en el vector valor.
				self.valor[-(i+1)] = num%10
				num = num//10
				self.can+=1
				if(num == 0): break
			
	def toString(self):
		print(f"{self.valor}, {self.size}, {self.base}")
	
	def __lt__(self, other):
		for i in range(self.size):
			if (self.valor[i] < other.valor[i]):
				return True
		return False
		
	def __gt__(self, other):
		for i in range(self.size):
			if (self.valor[i] > other.valor[i]):
				return True
		return False
	
	def __ge__(self, other):
		pass
	
	def __eq__(self, other):
		if(self.size == other.size and self.base == other.base):
			for i in range(self.size):
				if(self.valor[i] != other.valor[i]):
					return False
			return True
		else:
			return False
	
	def __repr__(self):
		aux = 0
		for i in range(self.can):
			aux+=self.valor[-(i+1)]*self.base**i
		return f"Numero({aux})"
		
	def __add__(self, other):
		#print("SUMANDO---", self.valor, other.valor)
		auxNum = Numero()
		carry = 0
		cont = max(self.can, other.can)
		try:
			for i in range (cont):	#Se elige el que tenga mayor cantidad, para completar la suma.

				auxNum.valor[-(i+1)] = self.valor[-(i+1)] + other.valor[-(i+1)]
				auxNum.can += 1
				auxNum.valor[-(i+1)] += carry

				carry = 0
				
				if(auxNum.valor[-(i+1)] > 9 and i < cont-1):	#Hay que hacer acarreo?
					carry = auxNum.valor[-(i+1)]//10
					auxNum.valor[-(i+1)] = auxNum.valor[-(i+1)]%10 


				if(auxNum.valor[-(i+1)] > 9 and i == cont-1):
					#---------Exception------------  Excepcion cuando la suma de los valores excede el tamaño(size) de los numeros.
					if(i == self.size-1):
						auxNum.valor[-(i+1)] = auxNum.valor[-(i+1)]%10
						raise OverflowError("Overflow: Se sobrepaso el limite del numero, el numero se reinicio")
					#------------------------------
					auxNum.valor[-(i+2)] += auxNum.valor[-(i+1)]//10
					auxNum.valor[-(i+1)] = auxNum.valor[-(i+1)]%10 

					auxNum.can += 1
					
					
			#print(auxNum.can)		
			return auxNum
				
				
		except Exception as error:		# Se controla la excepcion.
			#self.prt(error)

			return auxNum
					
	def __sub__(self, other):
		#print("RESTANDO: ", self, other)
		if self < other:
			return ~(other + ~self)
		else:
			return self + ~other	# Suma self, con rabo de chancho other... osea el complemento de other
		
	
	def __invert__(self):		# Toma un objeto numero y lo transforma al complemento, y lo retorna.
		aux = [9] * self.size
		for i in range(self.can):
			aux[-(i+1)] -= self.valor[-(i+1)]
		n = Numero()
		n.valor = aux

		n.can = self.size
		n += Numero(1)

		return n
				
	def prt(self, error):
		print(error)
		
	def setVector(self, vec):
		self.valor = [0]*self.size
		self.can=0
		for i in range(len(vec)):
			self.valor[-(i+1)]=vec[-(i+1)]
			self.can +=1
			
	def __mul__(self, other):
		carry = 0
		auxList = []	#Lista donde se guardan los valores para ser sumados... contiene objetos Numero
		
		for i in range(other.can):
			aux2 = Numero()
			aux2.can += i
			for j in range(self.can):
				aux2.valor[-(j+1+i)] = other.valor[-(i+1)] * self.valor[-(j+1)]	#Aqui se multiplica digito a digito
				aux2.can += 1	#se aumenta la cantidad del numero
				#print(aux2, "aux2", j)
				aux2.valor[-(j+1+i)] += carry	#Se suma el acarreo, si hay.
				carry = 0	# Reseteamos el carry
				#print(carry, "carry", j)

				#------------Casos------------
				if((j+i)==self.size-1):	# Caso donde se podria exceder el "size" del Numero
					aux2.valor[-(j+1+i)] = (aux2.valor[-(j+1+i)]%10)
					#print("ardilla")
					break;
				
				if(aux2.valor[-(j+1+i)] > 9 and j < self.can-1):		#Si hay que hacer acarreo?
					carry = (aux2.valor[-(j+1+i)]//10)	#Sacamos el valor digito a acarrear.
					aux2.valor[-(j+1+i)] = (aux2.valor[-(j+1+i)]%10)	#se guarda el digito que queda del calculo.
					#print("ardilla2")
					
				if(aux2.valor[-(j+1+i)] > 9 and j == (self.can-1)):		#Si el resultado de la multiplicacion es de 2 digitos pero es la ultima
					aux2.valor[-(j+1+i)] = (aux2.valor[-(j+1+i)])
					#print("ardilla3")
					break;
				#------------------------------
			auxList.append(aux2)
			#print(auxList)

			
		if(len(auxList) > 1):	#Aqui se suman los Numero, de la lista y se retorna.
			for i in range(len(auxList)-1): 
				auxList[0] = auxList[0] + auxList[i+1]
			return auxList[0]
		else:
			return auxList[0]
	
	def convertInt(self, a):
		n = len(a)
		aux = 0
		for i in range(n):
			aux += a[-(i+1)]*self.base**i
		return aux
	
	def __truediv__(self, other):
		try:
	
			dividendo = self.valor[-(self.can):]
			nuevoDividendo=[]
			residuo = 0
			resultado=[]
		
			if other == Numero(0):
				raise Exception ("Error: no se puede dividir entre cero")
			if other>self or self==Numero(0):#Si el divisor es mayor que el dividendo(CB)
				return Numero(0)
			if other==self:#Si el divisor es igual que el dividendo(CB)
				return Numero(1)
			if other==Numero(1):
				return self
					
			while dividendo!=[]:
				auxND=0
				nuevoDividendo.append(dividendo[0])
				auxND = self.convertInt(nuevoDividendo)
				
				if residuo==0:
						pass
				else:	
					nuevoDividendo.insert(0,residuo)
					auxND = self.convertInt(nuevoDividendo)
					residuo = 0
				
				if Numero(auxND) > other:
					contador=0
					contadorDividiendo=auxND
					
					while(Numero(contadorDividiendo)>=other):
					
						print(Numero(contadorDividiendo)>=other)
						print (contadorDividiendo)
						numerito=Numero(contadorDividiendo)-other
						print (numerito.valor)
						print (other.valor)
						contadorDividiendo=self.convertInt(numerito.valor)
						print (contadorDividiendo)
						print (other.valor)
						contador+=1
						print(other)
						print(Numero(contadorDividiendo)>=other)
					
					if (Numero(contadorDividiendo)!=Numero(0)):
						residuo=contadorDividiendo
					resultado.append(contador)
					nuevoDividendo = []
					
				if Numero(auxND) < other:
					if (len(resultado)==0 or len(dividendo)==1):
						pass
					if auxND == 0:
						resultado.append(0)
					else:
						resultado.append(0)
				if Numero(auxND) == other:
					resultado.append(1)
					nuevoDividendo=[]
				
				dividendo = dividendo[1:]
			
			
			aux = Numero()
			aux.setVector(resultado)
			return aux
		except Exception as error:		# Se controla la excepcion.
			return self.prt(error)
											
	def __lshift__(self, x):
		#print("a")
		a = 10**x
		return self * Numero(a)
		#elevado=10**other
		#numero=Numero(elevado)
		#return self*numero
	def __rshift__(self, x):
		try:
			if x>self.can:
				raise Exception ("EL numero va a quedar en decimal")
			if x==self.can:
				return Numero(0)
			else:
				for i in range (x):
					self.valor[-self.can]=0
					self.can-=1
				return self
					
		except Exception as error:		# Se controla la excepcion.
			return self.prt(error)		
				
				
				
				
				
				
			
			
	