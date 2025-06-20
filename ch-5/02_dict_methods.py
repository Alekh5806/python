# METHODS OF DICTIONARY

marks = {
    "alekh" : 20,
    "taksh" :16,
    "krunal" : 18,
    "rahil" : 16
}

print(marks,type(marks))
#it can't tell us the index but it can give the value of the store things 
print(marks["alekh"]) # output:20
#mathods of dictionary 
print(marks.items()) # it will print the all key pairs in the form of ('alekh', 20)
print(marks.keys()) # left end side are reffered as keys 
print(marks.values()) # right end sides are reffered as values 
marks.update({"alekh":19,"harsh":18}) # it will update the marks of alekh to 19 and if not present it will add it it dictbecause dictionary are mutable means changable 
print(marks)
print(marks.get("alekh")) # output:19
# THINGS TO REMEMBER
print(marks.get("alekh2")) # output : none
print(marks["alekh2"]) # Returns an error