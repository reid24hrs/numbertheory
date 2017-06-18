# program to implement the Euclidean algorithm to find greatest common divisor (gcd) of two integers

# gcd function

def gcd(a,b):

# make sure that a is less than or equal to b, otherwise swap them
   if a > b:
      temporary = a
      a = b
      b = temporary
   remainder = 1
   while(remainder > 0):
      result = remainder
      remainder = b % a
      quotient = (b - remainder)/a
      b = a
      a = remainder
   return(result)

# test the gcd function

a = input("Enter number a: ")
b = input ("Enter number b: ")

print'gcd(',a,',',b,') =',gcd(a,b)

