import timeit

def imp():
	v = [2]
	x = [2]
	return x

if __name__ == "__main__":
	v = 2
	x = 3
	y = timeit.timeit(imp)
	print (y)