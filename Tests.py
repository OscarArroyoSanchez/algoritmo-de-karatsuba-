"""
	Autores: Joy Bonilla, Oscar Arroyo, Natalia Solano, Jose Pablo Perez - 8AM
	
	Referencias:
			https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
			https://pythonhow.com/measure-execution-time-python-code/
			
"""
from Numero import *
from Knumero import *
import timeit
import random

def testNumero():
	print("------------------ Probando suma: ------------------------")
	for i in range (6):
		numero = random.randint(1, (10**i)+1)
		a = Numero(numero)
		numero2 = random.randint(1, (10**i)+1)
		b = Numero(numero2)
		print("Sumando: ", a, "+", b)
		print("R/", a+b, " - " "Resultado PYTHON: ", numero+numero2, "\n")
	
	print("\n")
	print("------------------ Probando resta: ------------------------")
	for i in range (6):
		numero = random.randint(1, (10**i)+1)
		a = Numero(numero)
		numero2 = random.randint(1, (10**i)+1)
		b = Numero(numero2)
		print("Restando: ", a, "-", b)
		print("R/", a-b, " - " "Resultado PYTHON: ", numero-numero2, "\n")
	
	print("\n")
	print("------------------ Probando Multiplicacion de escuela: ------------------------")
	for i in range (2, 10, 2):
		numero = random.randint(1, (10**i)+1)
		a = Numero(numero)
		numero2 = random.randint(1, (10**i)+1)
		b = Numero(numero2)
		print("Multiplicando: ", a, "*", b)
		print("R/", a*b, " - " "Resultado PYTHON: ", numero*numero2, "\n")
		
	print("\n")
	print("------------------ Probando Division: ------------------------")
	for i in range (6):
		numero = random.randint(1, (10**i)+1)
		a = Numero(numero)
		numero2 = random.randint(1, (10**i)+1)
		b = Numero(numero2)
		print("Dividiendo: ", a, "/", b)
		print("R/", a/b, " - " "Resultado PYTHON: ", numero//numero2, "\n")
		
	print("\n")
	print("------------------ Probando Multiplicacion por Karatsuba: ------------------------")
	for i in range (2, 10, 2):
		numero = random.randint(1, (10**i)+1)
		a = Knumero(numero)
		numero2 = random.randint(1, (10**i)+1)
		b = Knumero(numero2)
		print("Multiplicando: ", a, "*", b)
		print("R/", a*b, " - " "Resultado PYTHON: ", numero*numero2, "\n")
		
def timeNvK():
	with open("TestK.csv", "w") as file:
	file.write(f"N: ;AlgoritmoEscuela: ;AlgoritmoKaratsuba: \n")
	for i in range (5, 25):
		numero = random.randint(1, (10**i)+1)
		a = Knumero(numero)
		numero2 = random.randint(1, (10**i)+1)
		b = Knumero(numero2)
		
		TimeSchool = timeit.timeit("a*b", globals=globals(), number = 100)*1000
		TimeKaratsuba = timeit.timeit("a*b", globals=globals(), number = 100)*1000
		file.write(f"{a},{b};{TimeSchool};{TimeKaratsuba} \n")
		
if __name__ == "__main__":

	testNumero()
	timeNvK()
	
	