# class Dog:
#     def sound(self):
#         print("Dog barks")
# class Cat:
#     def sound(self):
#         print("Cat meows")
# dog1=Dog()
# cat1=Cat()
# dog1.sound()
# cat1.sound()

# class Animal:
#     def sound(Self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def sound(Self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(Self):
#         print("Cat meows")
# animals=[Animal(), Dog(), Cat()]
# for animal in animals:
#     animal.sound()
# def add(a, b=0, c=0):
#     return a+b+c
# print("add(5):", add(5))
# print("add(5,10):",add(5,10))
# print("add(5,10,15):", add(5,10,15))


class Student:
    def display(self):
        print("Student Details")
class Result(Student):
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
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