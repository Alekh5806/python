# Write a program to filter a list of numbers which is divisible by 5.

def divisible5(n):
  if(n%5 == 0):
    return True
  return False 

a = [1,2,44,55,66,77,88,34,46,90]

f = list(filter(divisible5,a))
print(f)