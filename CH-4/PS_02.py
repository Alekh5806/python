# write a program to accept marks of 6 students and display them in a sorted manner
studentsmarks = []
s1 = int(input("enter the marks of student 1: "))
studentsmarks.append(s1)
s2 = int(input("enter the marks of student 2: "))
studentsmarks.append(s2)
s3 = int(input("enter the marks of student 3: "))
studentsmarks.append(s3)
s4= int(input("enter the marks of student 4: "))
studentsmarks.append(s4)
s5 = int(input("enter the marks of student 5: "))
studentsmarks.append(s5)
s6 = int(input("enter the marks of student 6: "))
studentsmarks.append(s6)

print("original marks list: ",studentsmarks)
studentsmarks.sort()
print("sorted marks: ",studentsmarks)





