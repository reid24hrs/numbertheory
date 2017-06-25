# program to compute a**k (mod m) for large numbers

def powers(a1,k1,m1):
   running_total1 = a1
   running_exponent1 = 1
   while (running_exponent1 < k1):
      running_total1 = running_total1**2 % m1
      running_exponent1 = running_exponent1 * 2
   return(running_total1)

a = input("Enter number a: ")
k = input("Enter number k: ")
m = input("Enter number m: ")

running_total = 1
running_exponent = 1 # start with an exponent of 1

while (running_exponent <= k):
   if (k/(running_exponent) % 2)==1:
      factor = powers(a,running_exponent,m)	
      running_total = (running_total * factor) % m
   running_exponent = running_exponent * 2

print "result: ",running_total