#SMALLEST AMONG 10 NUMBERS
a=[45,21, 43, 78, 4, 98, 34, 65 ,29, 10]
s=a[0]
for i in a:
  if(i<s):
    s=i
print(s)
'''
OUTPUT
  4
'''

#SMALLEST AMONG 3 NUMBERS
a=54
b=71
c=95
if(a<=b and a<=c):
  min=a
elif(b<=a and b<=c):
  min=b
else:
  min=c
print(min)
'''
OUTPUT
  54
'''
