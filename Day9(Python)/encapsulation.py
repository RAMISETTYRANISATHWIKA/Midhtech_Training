#Encapsulation is the process of wrapping data(variables) and methods(functions) into a single unit(class) while restricting direct access to the object's data.
"""Access Specifiers:
1.public: name - Accessible from anywhere
2.protected: _name  - Accessible within class and derived classes(by convention)
3.private: __name  -  Accessible only within in the class(name mangling)
"""
#Task: Code using all the Access Specifiers 

# class BankAccount:
#     def __init__(self, owner, balance, bank_name, bank_address):
#         self.owner=owner
#         self.__balance=balance
#         self.bank_name=bank_name
#         self.bank_address=bank_address
#     def show_balance(self):
#         print("Owner:", self.owner)
#         print("Balance:", self.__balance)
#         print("Bank name:", self.bank_name)
#         print("Bank Address:", self.bank_address)
# account1=BankAccount("Ram", 50000, "Abc Bank", "Abc")
# account1.show_balance()

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.__marks = marks
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.__marks)
        if self.__marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")

s1 = Student("Ravi", 20, 75)
s1.display()
       