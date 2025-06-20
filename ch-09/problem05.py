# Repeat program 4 for a list of such words to be censored.
words = ["donkey","bad","ganda"]

with open("/Users/alekh/Desktop/python/ch-09/donkeyfile.txt","r") as f:
  content = f.read()
for word in words:
    content = content.replace(word,"#"*len(word))

with open("/Users/alekh/Desktop/python/ch-09/donkeyfile.txt","w") as f:
  f.write(content)