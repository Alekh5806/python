# Add a static method in problem 2, to greet the yser with hello.


class calculator:
  def __init__(self,n):
    self.n = n
  def square(self):
    print(f"The square is {self.n*self.n}")
    
  def cube(self):
    print(f"The cube is {self.n*self.n*self.n}")
    
  def squareroot(self):
    print(f"The squareroot is {self.n**(1/2)}")  # here ** is used to make the power coeff here that is raised to 1/2
  
  @staticmethod
  def greet():
    print("good morning..")

a = calculator(4)
a.greet()
a.square()
a.cube()
a.squareroot()