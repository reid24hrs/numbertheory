# program to explore congruence 

m = input("Enter number m: ")
table = [[0 for x in range(m+1)] for y in range(m)]

for i in range(m+1):
	print i+1,
print
for a in range(m):
   for k in range (m+1):
#	   table[a][k]= a**k
      print a**(k+1)%m,
   print