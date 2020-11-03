#BINARY TO DECIMAL
def bintodec(bin):
  i,decimal=0,0
  while(bin!=0):
    dec=bin%10
    decimal=decimal+dec*pow(2,i)
    bin=bin//10
    i+=1
  return(decimal)
print(bintodec(1001))
'''
OUTPUT
  9
'''

#DECIMAL TO BINARY
def dectobin(dec):
  if(dec>1):
    dectobin(dec//2)
  print(dec%2,end="")
dectobin(9)
'''
OUTPUT
  1001
'''
