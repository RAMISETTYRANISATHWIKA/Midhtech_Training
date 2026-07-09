#Single Inheritance
class Person:
    def display(self):
        print("I am a Person")
class Student(Person):
    def show(self):
        print("I am a Student")
s=Student()
s.display()
s.show()

#Multiple Inheritance
class Father:
    def father(self):
        print("Father's Property")
class Mother:
    def mother(self):
        print("Mother's Property")
class Child(Father,Mother):
    def child(self):
        print("Child's Property")
c=Child()
c.father()
c.mother()
c.child()

#Multilevel Inheritance
class Grandfather:
    def grand(self):
        print("Grandfather")
class Father(Grandfather):
    def father(self):
        print("Father")
class Son(Father):
    def son(self):
        print("Son")
s=Son()
s.grand()
s.father()
s.son()

#Hierarchical Inheritance
class Person:
    def display(self):
        print("I am a Person")
class Student(Person):
    def student(self):
        print("I am a Student")
class Teacher(Person):
    def teacher(self):
        print("I am a Teacher")
s=Student()
s.display()
s.student()
t=Teacher()
t.display()
t.teacher()

#Hybrid Inheritance
class A:
    def showA(self):
        print("Class A")
class B(A):
    def showB(self):
        print("Class B")
class C(A):
    def showC(self):
        print("Class C")
class D(B,C):
    def showD(self):
        print("Class D")
d=D()
d.showA()
d.showB()
d.showC()
d.showD()