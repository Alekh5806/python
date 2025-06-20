# if the languages of 2 friends are same; what will happen to the program in problem 6 
# create a dictionary.Allow 4 friends to enter their favourite language as value and use key as their names.Assume that the name are unique 
dic = {}
name = input("enter friend's name: ")
lang = input("enter language name: ")
dic.update({name:lang})
name = input("enter friend's name: ")
lang = input("enter language name: ")
dic.update({name:lang})
name = input("enter friend's name: ")
lang = input("enter language name: ")
dic.update({name:lang})
name = input("enter friend's name: ")
lang = input("enter language name: ")
dic.update({name:lang})
print(dic)
#nothing will happen values can be same 