#GCD OF TWO NUMBERS USING RECURSION
def findgcd(a,b):
  if(b==0):
    return a
  else:
    return findgcd(b,a%b)
print(findgcd(4,2))
'''
OUTPUT
  2
'''


#GCD OF TWO NUMBERS USING LOOP
def findgcd(a,b):
  while(b!=0):
    temp=b
    b=a%temp
    a=temp
  return a
print(findgcd(20,30))
'''
OUTPUT
  10
'''

#GCD FOR ARRAY OF ELEMENTS
def findgcd(a,b):
  if(b==0):
    return a
  else:
    return findgcd(b,a%b)
    
arr=[8,16,20,32]
a1=arr[0]
a2=arr[1]
gcd=findgcd(a1,a2)
for i in range(2,len(arr)):
  gcd=findgcd(gcd,arr[i])
print(gcd)
'''
OUTPUT
  4
'''
