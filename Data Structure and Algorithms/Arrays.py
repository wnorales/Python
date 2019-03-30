from array import *

array1 = array('i', [10, 20, 30, 40, 50, 80])

for x in array1:
    print(x)
# Printing specific Elements from an Array
print(array1[0])
print(array1[2])
# Inserting Elements into an Array
array1.insert(1, 15)
for x in array1:
    print(x)
# Removing from an Array
array1.remove(50)
for x in array1:
    print(x)
# Search in an Array, This will return the index of an Element
print(array1.index(15))
# Updating an element in an Array
array1[5] = 90
for x in array1:
    print(x)