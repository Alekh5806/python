class Employee:
  language = "Python"
  salary = 1600000

  def __init__(self,name,salary,language): # dunder method
    self.name = name
    self.salary = salary
    self.language = language
    print("I am creating an object..")

alekh = Employee("Alekh",1600000,"Java")
print(alekh.name,alekh.salary,alekh.language)

    