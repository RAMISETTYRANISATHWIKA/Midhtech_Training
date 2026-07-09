#Constructor is a special method that runs automatically when an object is created.
#In python, it is written using __init__()
#It is mainly used to initialize object data such as name, age, balance or price

class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
s1=Student("Ram", 20)
s1.display()

        