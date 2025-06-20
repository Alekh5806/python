# negative slicing in python 
name = "Alekh"
print(name[0:3]) # it will print Ale
print(name[-4:-1]) # it will start indexing from end means -1 is starting from the end so it will prints lekh
print(name[-1:-4]) # it will start indexing from end means -4 is starting from the end so it will prints nothing
print(name[:4])  # is same as print(name[0:4])
print(name[1:])  # is same as print(name[1:5])