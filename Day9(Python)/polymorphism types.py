#Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
d=Dog()
d.sound()

#Method Overloading
class Calculator:
    def add(self,a,b=0):
        print(a+b)
c=Calculator()
c.add(10)
c.add(10,20)