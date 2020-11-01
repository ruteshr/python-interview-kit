'''Definition
Bubble Sort is the simplest sorting alogrorithm that works by repeatedly swapping the adjacent element if the first element is greater than the second element.
'''
def bubblesort(a):
  for i in range(len(a)-1,0,-1):
    for j in range(i):
      if(a[j]>a[j+1]):
        temp=a[j]
        a[j]=a[j+1]
        a[j+1]=temp  
  return(a)
a=[2, 7, 1, 5, 3]
print(bubblesort(a))
'''
OUTPUT
  [1, 2, 3, 5, 7]
'''

