#FACTORIAL USING LOOP
n=5
fact=1
while(n>0):
  fact*=n
  n-=1
print(fact)
'''
OUTPUT
  120
'''


#FACTORIAL USING RECURSION
def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)
n=5
print(factorial(n))
'''
OUTPUT
  120
'''
