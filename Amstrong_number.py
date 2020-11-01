#AMSTRONG NUMBER CHECK
'''
In case of 3 digit, if the sum of cube of each digit is equal to the number itself. Then it is called Amstrong Number
'''
n=1634
ord=len(str(n))
sum=0
temp=n
while(temp>0):
  a=temp%10
  sum+=a**ord
  temp=temp//10
if(n==sum):
  print(n,"is an Amstrong number")
else:
  print(n," is not an Amstrong number")
'''
OUTPUT
  1634 is an Amstrong number
'''
