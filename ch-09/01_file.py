# in open fun the default function of file is in read mode so we don't have to wite the r mode but if we want to open the file in write mode we had to write f = open("file.txt","w")
f = open("file.txt")
data = f.read()
print(data)
f.close()
