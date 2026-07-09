class Animal:
    def eat(self):
        print("Animal eats food")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Cat(Animal):
    def meows(self):
        print("Cat Meows")
class Cow(Animal):
    def moo(self):
        print("Cow moos")
class Lion(Animal):
    def roar(self):
        print("Lion roars")
dog1=Dog()
dog1.eat()
dog1.bark()

cat1=Cat()
cat1.eat()
cat1.meows()

cow1 = Cow()
cow1.eat()
cow1.moo()

lion1 = Lion()
lion1.eat()
lion1.roar()

""" 
Name:Ravi
Age:20
Marks:75
Result:Pass
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Result(Student):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")
s1 = Result("Ravi", 20, 75)
s1.display()

           






