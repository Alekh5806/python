# write a program to display a/b where a and b are integers. if b=0 , display infinite by handling the 'ZeroDivisionError'
try:
  a = int(input("enter a: "))
  b = int(input("enter b: "))
  print(a/b)
except ZeroDivisionError as v:
  print("Infinite")