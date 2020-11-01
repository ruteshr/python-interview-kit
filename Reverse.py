#REVERSE AN ARRAY OF NUMBERS/STRING
arr=[1,3,4,5]
newarr=arr[::-1]
print(newarr)
'''
OUTPUT
  [5, 4, 3, 1]
'''

#REVERSE AN STRING USING LOOP
s='Reverse'
st=""
for i in s:
    st=i+st
print(st)
'''
OUTPUT
    esreveR
'''

#REVERSE AN STRING USING RECURSION
def revstring(s):
  if(len(s)==0):
    return s
  else:
    return revstring(s[1:]) +s[0]
s='RecursionReverse'
print(revstring(s))
'''
OUTPUT
  esreveRnoisruceR
'''

#REVERSE A NUMBER
def revnum(n):
  rev=0
  while(n>0):
    rev=rev*10 + n%10
    n=n//10
  return rev
n=12345
print(revnum(n))
'''
OUTPUT
  54321
'''
