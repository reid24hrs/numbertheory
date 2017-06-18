# find Pythagorean triples where a,b & c are natural numbers and a**2 + b**2 = c**2

for a in range(1,1000): # start with a = 1 not 0 as in normal in python indexes
	for b in range(1,1000):
		for c in range(1,1000):
			if ((a**2 + b**2)==c**2):
				print a, ", ",b,", ",c,", a**2 + b**2 = ",a**2 + b**2, c**2
