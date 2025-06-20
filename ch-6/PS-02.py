# Write a program to find out whether the student had passed or failed if it requires a total of 40% and at least 33% in each subject to pass.Assume 3 subjects and take marks as an input from the user 
marksS1 = int(input("enter the marks of subject1: "))
marksS2 = int(input("enter the marks of subject2: "))
marksS3 = int(input("enter the marks of subject3: "))
totalmarks = (100*(marksS1+marksS2+marksS3))/300

if(totalmarks>=40 and marksS1>=33 and marksS2>=33 and marksS3>=33):
  print("congratulation you had pass the exam...",totalmarks)
else:
  print("Better luck next time....",totalmarks)