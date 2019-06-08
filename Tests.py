"""
	Autores: Joy Bonilla, Oscar Arroyo, Natalia Solano, Jose Pablo Perez - 8AM
"""
from Numero import *
from Knumero import *

if __name__ == "__main__":
	num = Numero(num=12, tam=16, base=10)
	#num.toString()
	num2 = Numero(num=123, tam=16, base=10)
	#num3 = Numero (2567, 10, 6)
	#print(num - num2, "Test1", "\n")
	
	num3 = Knumero(2004)
	num4 = Knumero(1998)
	#print(num3.valor, "knum")
	#print(num + num2, "Test2")
	#print(num3 * num4, "Test")
	#print(num3 * num4, "Resultado")
	print(num2*num)
	