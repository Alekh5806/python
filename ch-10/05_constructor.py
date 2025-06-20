class Employee:
  language = "python"
  salary = 1600000
  
  def __init__(self): # dunder method which is automatically called
    print("I am creating an object")

  def getinfo(self):
    print(f"the language is {self.language} and the salary is {self.salary}")

  @staticmethod
  def greet():
    print("Good morning")

alekh = Employee()
alekh.name = "alekh"
alekh.getinfo()
alekh.greet()

harry = Employee()