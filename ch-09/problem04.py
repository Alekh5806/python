# A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ###### by updating the same file.
word = "donkey"

with open("/Users/alekh/Desktop/python/ch-09/donkeyfile.txt","r") as f:
  content = f.read()

contentNew = content.replace(word,"######")

with open("/Users/alekh/Desktop/python/ch-09/donkeyfile.txt","w") as f:
  f.write(contentNew)