a = int(input("enter your age: "))
# the space{intended space} below the condition is showing that you are inside the condition for exiting it remove the condition
# if elif else ladder
if(a>=18):
  print("you are eligible for applying driving license..")
  print("go and apply as soon as possible")
elif(a<0):
  print("you are entering the negative value plz correct it..")
elif(a==0):
  print("you are entering the zero which is not valid..")
else:
  print("you are not eligible for applyong driving license..")

print("end of program..")