# Write a program to make a copy of a text file "this. txt"

with open("/Users/alekh/Desktop/python/ch-09/this.txt","r") as f:
  content = f.read()

with open("/Users/alekh/Desktop/python/ch-09/this_copy.txt","w") as f:
  f.write(content)