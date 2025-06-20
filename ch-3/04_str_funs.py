name = "alekh"
print(len(name)) # it will be 5 
print(name.endswith("kh"))  # it will print true because it is ending with kh 
print(name.endswith("ae"))  # it will print false because it is not ending with ae

# this all string functions are case-sensitive 

print(name.startswith("A")) # it will give false because of case sensitive 
print(name.startswith("a")) # it will give true because it is starting with "a"