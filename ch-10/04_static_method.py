# Sometimes we need a function that does not use the self-parameter. We can define a static method like this:
class Employee:
  language = "python"
  salary = 1600000
  
  @staticmethod
  def greet():
    print("good morning..")

alekh = Employee()
alekh.greet()