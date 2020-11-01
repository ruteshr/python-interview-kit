#PRIME NUMBER CHECK
n=11
if(n>1):
  for i in range(2,n//2):
    if(n%i==0):
      print(n,"not a prime number")
      break
  else:
    print(n,"is a prime number")
else:
  print(n, "is not a prime number")
'''
OUTPUT
  11
'''

#PRINTING PRIME NUMBER B/W INTERVAL
start=100
end=150
for x in range(start,end+1):
  if(x>1):
    for i in range(2,x//2):
      if(x%i==0):
        break;
    else:
      print(x,end=" ")
  else:
    break
'''
OUTPUT
  101 103 107 109 113 127 131 137 139 149
'''
