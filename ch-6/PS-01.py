# Write a program to find out the greatest of four number entered by the user 
num1 = int(input("enter the num1 you want to check: "))
num2 = int(input("enter the num2 you want to check: "))
num3 = int(input("enter the num3 you want to check: "))
num4 = int(input("enter the num4 you want to check: "))
if(num1>num2 and num1>num3 and num1>num4):
  print("num1 is greatest of all the number..")
elif(num2>num1 and num2>num3 and num2>num4):
  print("num2 is greatest of all the number..")
elif(num3>num1 and num3>num2 and num3>num4):
  print("num3 is greatest of all the number..")
else:
  print("num4 is greatest of all the number.. ")

print("end of the program...........")

