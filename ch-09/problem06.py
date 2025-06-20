# Write a program to mine a log file and find out whether it contains 'python'.
with open("/Users/alekh/Desktop/python/ch-09/log.txt","r") as f:
  content = f.read()

if("python" in content):
  print("Yes python is present")
else:
  print("python is not present")
