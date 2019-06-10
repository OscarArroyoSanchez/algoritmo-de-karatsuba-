"""
	Autores: Joy Bonilla, Oscar Arroyo, Natalia Solano, Jose Pablo Perez - 8AM
	
	Referencias:
			https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
			https://pythonhow.com/measure-execution-time-python-code/
			
"""
from Numero import *
from Knumero import *
import timeit



if __name__ == "__main__":
	num = Numero(num=12, tam=16, base=10)
	#num.toString()
	num2 = Numero(num=14, tam=16, base=10)
	
	num3 = Knumero (99)
	num4 = Knumero(1998)
	#print(num - num2, "Test1", "\n")
	#print(num3.valor, "knum")
	#print(num + num2, "Test2")
	#print(num3 * num4, "Test")
	#print(num3 * num4, "Resultado")
	#print(num3, num4)
	print(num3 * num4)
	#print("Resultado: ", num > num2)
	#print (num * num2)
	"""
	with open("TestK.csv", "w") as file:
		file.write(f"AlgoritmoEscuela: ;AlgoritmoKaratsuba: \n")
		for i in range (1, 9999999999, 99999998):
			
			TimeSchool = timeit.timeit("Numero(i)*Numero(i)", globals=globals(), number = 1000)
			TimeKaratsuba = timeit.timeit("Knumero(i)*Knumero(i)", globals=globals(), number = 1000)
			file.write(f"{TimeSchool};{TimeKaratsuba} \n")
	
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