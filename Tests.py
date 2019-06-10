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
		
if __name__ == "__main__":
	num = Numero(num=500, tam=16, base=10)
	#num.toString()
	num2 = Numero(num=25, tam=16, base=10)
	
	num3 = Knumero (294)
	num4 = Knumero(627)
	#print(num - num2, "Test1", "\n")
	#print(num3.valor, "knum")
	#print(num + num2, "Test2")
	#print(num3 * num4, "Test")
	#print(num3 * num4, "Resultado")
	#print(num3, num4)
	#print(num3 * num4)
	#print("Resultado: ", num > num2)
	#print (num.valor)
	#print (num2.valor)
	#print (num / num2)
	#print (num>num2)
	testNumero()
	
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
		
	"""
	with open ("Test.csv", "w") as file:
		with open ("Prueba.csv", "r") as cases:
			doc = cases.readlines() 
			file.write(f"Numero 1;x;Numero 2;Tiempo Karatsuba;Tiempo Multiplicacion;Resultado Karatsuba;Resultado Multiplicacion\n")
			for line in doc:
				case = line.split(";")
				num1 = Numero(num = int(case[0]),tam = 16, base = 10)
				num2 = Numero(num = int(case[1]),tam = 16, base = 10)
				num3 = Knumero(int(case[0]))
				num4 = Knumero(int(case[1]))
				#Toma el tiempo de multiplicacion regular
				start = time.time()
				for i in range(100):
					rm = num1 * num2
				end = time.time()
				tm = end - start
				#Toma el tiempo de multiplicacion karatsuba
				start1 = time.time()
				for i in range(100):
					rk = num3 * num4
				end1 = time.time()
				tk = end1 - start1
				file.write(f"{num1};x;{num2};{tk};{tm};{rk};{rm}\n")
	"""