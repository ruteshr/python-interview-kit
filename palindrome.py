#PALINDROME CHECK (STRING)
s="malayalam"
ns=""
for i in s:
    ns=i+ns
if(s==ns):
    print("pallindrome")
else:
    print("not a pallindrome")
'''
OUTPUT
    pallindrome
'''


#PALINDROME CHECK (NUMBER)
def palin(num):
  rev=0
  while(num>0):
    rev=rev*10 + num%10
    num=num//10
  return rev
num=4114
check=palin(num)
if(check==num):
    print("pallindrome")
else:
  print("not a pallindrome")
'''
OUTPUT
    pallindrome
'''
