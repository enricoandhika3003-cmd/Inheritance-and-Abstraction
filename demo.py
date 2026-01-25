class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def info(self):
        print("Name = ", self.name, ", ID = ", self.idnumber)

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)

e = Employee("Enrico", 1234567890, "$123", "Human Resources")
e.info()

class Person2:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname, self.lname)
        
class Student(Person2):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation = year

s = Student("Bienve", "Caton", 2023)
s.printname()


from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animals):
    def move(self):
        print("Walk")

class Horse(Animals):
    def move(self):
        print("Gallop")

class Rabbit(Animals):
    def move(self):
        print("Jump")

class Dog(Animals):
    def move(self):
        print("Pounce")

h = Human()
h.move()

import math
class Shapes:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

class Square(Shapes):
    def __init__(self, name, sides, length):
        self.length = length
        Shapes.__init__(self, name, sides)
    
    def calculate(self):
        if float(self.length)<0:
            print(f"Invalid side length for the {self.name}")
        elif int(self.sides)==4:
            print(f"The area of a {self.name} with side length {self.length} units is: {(self.length)**2} units^2")
        else:
            print(f"Invalid number of sides for the {self.name}")

class Rectangle(Shapes):
    def __init__(self, name, sides, length, width):
        self.length = length
        self.width = width
        Shapes.__init__(self, name, sides)
    
    def calculate(self):
        if float(self.length)<0 or float(self.width)<0:
            print(f"Invalid length or width for the {self.name}")
        elif int(self.sides)==4:
            print(f"The area of a {self.name} with length {self.length} units and width {self.width} units is: {(self.length)*(self.width)} units^2")
        else:
            print(f"Invalid number of sides for the {self.name}")

class Circle(Shapes):
    def __init__(self, name, sides, radius):
        self.radius = radius
        Shapes.__init__(self, name, sides)
    
    def calculate(self):
        if float(self.radius)<0:
            print(f"Invalid radius for the {self.name}")
        elif int(self.sides)==0:
            print(f"The area of a {self.name} with radius {self.radius} units and diameter {(self.radius)*2} units is: {((self.radius)**2)*math.pi} units^2")
        else:
            print(f"Invalid number of sides for the {self.name}")
            

sq = Square("Square", 4, -17)
sq.calculate()

sq2 = Square("Square", 3, 8)
sq2.calculate()

sq3 = Square("Square", 4, 9.5)
sq3.calculate()

r = Rectangle("Rectangle", 4, -5, 7)
r.calculate()

r2 = Rectangle("Rectangle", 3, 4, 9)
r2.calculate()

r3 = Rectangle("Rectangle", 4, 5.5, 6)
r3.calculate()

c = Circle("Circle", 0, -10)
c.calculate()

c2 = Circle("Circle", 1, 3)
c2.calculate()

c3 = Circle("Circle", 0, 5)
c3.calculate()