f = open("/Users/alekh/Desktop/python/ch-09/1stfile.txt","r")
lines = f.readlines()
print(lines,type(lines))
f.close()