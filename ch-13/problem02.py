# Write a program to input name, marks and phone number of a student and format it using the format function like below 
# " The name of the student is Alekh, his marks are 80 and phone number is 9925070999"

name = input("Enter your name here: ")
marks = int(input("Ente your marks here: "))
phoneNo = int(input("Enter your phone no: "))

data = "The name of the student is {}, his marks are {} and phone number is {}". format(name,marks,phoneNo)
print(data)