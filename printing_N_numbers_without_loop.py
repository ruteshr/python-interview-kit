#printing n numbers without loop

def myloop(n):
  if(n>0):
    myloop(n-1)
    print(n)
myloop(10)
'''
OUTPUT:
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
'''
