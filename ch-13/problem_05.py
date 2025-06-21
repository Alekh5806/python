# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
a = [111,2,65,444,55,66,77,88,34,46,90]

def greater(a,b):
  if (a > b):
    return a
  return b

print(reduce(greater,a))