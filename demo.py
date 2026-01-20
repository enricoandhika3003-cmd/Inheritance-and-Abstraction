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
    def abs_method(self):
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