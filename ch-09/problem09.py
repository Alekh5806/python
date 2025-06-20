# Write a program to find out whether a file is identical & matches the content of another file.

with open("/Users/alekh/Desktop/python/ch-09/this.txt","r") as f:
  content1 = f.read()
with open("ch-09/this_copy.txt","r") as f:
  content2 = f.read()

if(content1 == content2):
  print("this content is matching or identical with another file")
else:
  print("no this is not the matching or identical content")