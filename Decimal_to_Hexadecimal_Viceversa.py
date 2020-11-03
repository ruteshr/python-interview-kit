#DECIMAL TO HEXADECIMAL
def dectohex(dec):
  if(dec>1):
    dectobin(dec//16)
  dec=dec%16
  if(dec==10):
    s='A'
  elif(dec==11):
    s='B'
  elif(dec==12):
    s='C'
  elif(dec==13):
    s='D'
  elif(dec==14):
    s='E'
  elif(dec==15):
    s='F'
  else:
    s=dec
  print(s,end="")
dectohex(26)
'''
OUTPUT
  1A
'''

