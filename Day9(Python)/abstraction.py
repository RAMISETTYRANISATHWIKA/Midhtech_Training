# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner=owner
#         self._account_type="savings"
#         self.__balance=balance
#     def deposit(self, amount):
#         if amount>0:
#             self.__balance+=amount
#     def withdraw(self, amount):
#         if 0<amount<=self.__balance:
#             self.__balance-=amount
#             print("Withdrawal Successfull")
#         else:
#             print("Insufficent balance or Inavalid amount")
#     def show_balance(self):
#         print("Balance:", self.__balance)
# account=BankAccount("Ram",100000)
# print("Owner:", account.owner)
# print("Acoount_type:", account._account_type)
# account.deposit(500)
# account.withdraw(300)
# account.show_balance()

# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(Self):
#         pass
# class Car(Vehicle):
#     def start(Self):
#         print("Car starts with a key")
# Car1=Car()
# Car1.start()

from abc import ABC, abstractmethod
class Student(ABC):
    @abstractmethod
    def display(self):
        pass
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