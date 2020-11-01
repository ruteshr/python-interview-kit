#LCM OF TWO NUMBERS
def findgcd(a,b):
  if(b==0):
    return a
  else:
    return findgcd(b,a%b)
    
def findlcm(a,b):
  return((a*b)/findgcd(a,b))
 
a=20
b=40
c=findlcm(a,b)
print(int(c))
'''
OUTPUT
  40.0
'''


def findgcd(a,b):
  if(b==0):
    return a
  else:
    return findgcd(b,a%b)
    
def findlcm(a,b):
  return((a*b)/findgcd(a,b))
arr=[2, 7, 3, 9, 4]
a1=arr[0]
a2=arr[1]
lcm=findlcm(a1,a2)
for i in range(2,len(arr)):
    lcm=findlcm(lcm,arr[i])
print(int(lcm))
'''
OUTPUT
  252
'''
