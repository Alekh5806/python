class Employee:
  language = "python"# This is a class attribute
  salary = 1600000

alekh = Employee()
alekh.name = "Patel Alekh" # This is a instance attribute
print(alekh.name,alekh.language,alekh.salary)

harry = Employee
harry.name = "Harry sir"
print(harry.name,harry.salary,harry.language)

# here name is instance attribute and salary and language are class attributes as they belongs to class 