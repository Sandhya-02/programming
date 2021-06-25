class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class jak(Person):
  firstname ="jak"
  pass

x = Person("bindhu", "sandhya") 
x.printname()


x = jak("Manasa", "tanusree")
x.printname()

