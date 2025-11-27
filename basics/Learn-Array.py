

from array import *

arr1 = array('i',[33,44,55,66,77])

print(type(arr1))
print(arr1)

arr1.append(88) # add 88 of the end array
# arr1.reverse() # [88, 77, 66, 55, 44, 33]

arr2 = array(arr1.typecode, arr1.tolist()) # create new array from arr1 with same type 'i'
arr3 = array(arr1.typecode,(n for n in arr1))

print(arr1.tolist())
print(arr2.tolist())
print(arr3.tolist())
