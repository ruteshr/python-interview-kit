#CHECKING LEAP YEAR
year=2000
if(year%4==0):
  if(year%100==0):
    if(year%400==0):
      print("leap year")
    else:
      print("Not a leap year")
  else:
    print("leap year")
else:
  print("Not a leap year")
'''
OUTPUT
  leap year
'''
