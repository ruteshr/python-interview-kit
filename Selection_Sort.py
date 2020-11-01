'''
DEFININITION:
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted part is picked and moved to the sorted part.
'''
#SELECTION SORT - ASCENDDING ORDER
def selectionsort(a):
  for i in range(len(a)-1):
    minpos=i
    for j in range(minpos,len(a)):
      if(a[j]<a[minpos]):
        minpos=j
    temp=a[i]
    a[i]=a[minpos]
    a[minpos]=temp
  return(a)
a=[3,1,6,4,9]
print(selectionsort(a))
'''
OUTPUT
    [1, 3, 4, 6, 9]
'''


#SELECTION SORT - DESCENDING ORDER
def selectionsort(a):
  for i in range(len(a)-1):
    minpos=i
    for j in range(minpos,len(a)):
      if(a[j]>a[minpos]):
        minpos=j
    temp=a[i]
    a[i]=a[minpos]
    a[minpos]=temp
  return(a)
a=[3,1,6,4,9]
print(selectionsort(a))
'''
OUTPUT
    [9, 6, 4, 3, 1]
'''
