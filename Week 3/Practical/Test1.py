
import sys

list1=["hello", 1, True]

print (list1)

list2=sys.argv[1:]

print (list2)

list1.extend(list2)
print(list1)