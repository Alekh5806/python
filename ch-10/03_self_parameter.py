# self refers to the instance of the class. It is automatically passed with a 
# function call from an object.

class Employee:
  language = "Python"
  salary = 1600000

  def getinfo(self):
    print(f"The language is {self.language} and\n \tThe salary is {self.salary}")
  def greet(self):
    print(f"good morning,{self.name}")


alekh = Employee()
alekh.name = "alekh"
#alekh.language = "Java" # this is an instance attribute 
alekh.getinfo()
# Employee.getinfo(alekh) is same as alekh.getinfo()
alekh.greet()