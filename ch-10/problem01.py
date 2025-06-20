# Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmers:
  language = "Python"
  project = "xyz"
  salary = 1000000

  def __init__(self,language,project,salary):
    self.language = language
    self.project = project 
    self.salary = salary

a = Programmers("java","webapp",1600000)
print(a.language,a.project,a.salary)
r = Programmers("c++","iosapp",1800000)
print(r.language,r.project,r.salary)
n = Programmers("javascript","Ui",1200000)
print(n.language,n.project,n.salary)

