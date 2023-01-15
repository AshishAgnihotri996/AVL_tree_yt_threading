import sys

a = [1,2,3,4,5]
b = [1,2,3,4,5]
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(a is b)  # id is checked
print(a==b) # value is checked