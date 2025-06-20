# write a python program to rename a file to "renamed_by_python.txt".
with open("/Users/alekh/Desktop/python/ch-09/old.txt","r") as f:
  content = f.read()

with open("renamed_by_python.txt","w") as f:
  f.write(content)