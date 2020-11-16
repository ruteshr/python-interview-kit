#FIBONACCI USING RECURSION
def fibonacci(n):
  if(n<0):
    print("Wrong Input")
  elif(n==1):
    return 0
  elif(n==2):
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)
n=9
for i in range(1,n+1):
  print(fibonacci(i))
'''
OUTPUT
  0 1 1 2 3 4 8 13 21
'''


#FIBONACCI WITHOUT RECURSION
n=9
a=0
b=1
if(n<=0):
  print("wrong input")
elif(n==1):
  print(a)
elif(n==2):
  print(a,b)
else:
  print(a,b,end=" ")
  while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n-=1
'''
OUTPUT
  0 1 1 2 3 4 8 13 21
'''
