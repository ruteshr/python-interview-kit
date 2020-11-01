#CHECKING ODD/EVEN NUMBER
n=53
if(n%2==0):
  print(n,"is an even number")
else:
  print(n,"is an odd number")
'''
OUTPUT
  53 is an odd number
'''


#PRINTING ODD NUMBER B/W THE INTERVAL
start=10
end=20
for i in range(start,end+1):
    if(i%2!=0):
      print(i,end=" ")
'''
OUTPUT
  11 13 15 17 19
'''


#PRINTING EVEN NUMBER B/W THE INTERVAL
start=10
end=20
for i in range(start,end+1):
    if(i%2==0):
      print(i,end=" ")
'''
OUTPUT
  10 12 14 18 20
'''
