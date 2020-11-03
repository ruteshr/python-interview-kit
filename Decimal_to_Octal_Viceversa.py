#DECIMAL TO OCTAL
def dectooct(dec):
  if(dec>1):
    dectooct(dec//8)
  print(dec%8,end="")
dectooct(30)
'''
OUTPUT
  36
'''

#OCTAL TO DECIMAL
def octtodec(oct):
  i,octal=0,0
  while(oct!=0):
    a=oct%10
    octal=octal+a*pow(8,i)
    oct=oct//10
    i+=1
  return octal
print(octtodec(36))
'''
OUTPUT
  30
'''
    
