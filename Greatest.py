#GREATEST AMONG 10 NUMBERS
a=[45,21, 43, 78, 4, 98, 34, 65 ,29, 0]
ma=a[0]
for i in a:
  if(i>ma):
    ma=i
print(ma)
'''
OUTPUT
  98
'''

#GREATEST AMONG 3 NUMBERS
a=54
b=71
c=95
if(a>=b and a>=c):
  max=a
elif(b>=a and b>=c):
  max=b
else:
  max=c
print(max)
'''
OUTPUT
  95
'''
