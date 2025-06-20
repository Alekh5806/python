# write a program to detect the double space in a string 
name = "alekh is a good  boy"
print(name.find("  ")) # it will find the index in statement where the double space is present 
# problem 04
#replace the double space from problem 3 with single space 
print(name.replace("  "," "))
# the original string will not change the new string will be printed without touching the original one 
print(name) # it will print the original string THEY ARE IMMUTABLE
