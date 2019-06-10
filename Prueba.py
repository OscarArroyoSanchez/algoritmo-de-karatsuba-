import timeit

def imp():
	v = [2]
	x = [2]
	return x

if __name__ == "__main__":
	v = 2
	x = 3
	y = timeit.timeit(imp)
	
	#123456
	#000567
	
	z2 = 123 * 0
	z0 = 456 * 567
	z1 = (((123+456)*(0+567)) -z2) -z0
	
	r = (z2*(10**(3*2)))+(z1*(10**3))+z0
	print (r)
	print (123456*567)