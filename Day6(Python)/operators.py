#Arithmetic Operators
sub1=int(input("Enter Marks:"))
sub2=int(input("Enter Marks:"))
sub3=int(input("Enter Marks:"))
sub4=int(input("Enter Marks:"))
sub5=int(input("Enter Marks:"))
sub6=int(input("Enter Marks:"))
sum1=sub1+sub2+sub3+sub4+sub5+sub6
percentage=(sum1/600)*100
print(f"The percentage of {sub1}, {sub2}, {sub3}, {sub4}, {sub5}, {sub6} is {percentage}")

#Assignment Operators
wallet=500
wallet-=120
wallet+=200
print(f"Final Wallet Balance is {wallet}")

#Comparision Operators
#Program-1
person1=500
person2=500
print(person1==person2)

#Program-2
marks=98
pass_marks=35
print(marks>= pass_marks)


#Logical Operators
#Program-1
marks=int(input("Enter Marks:"))
attendance=int(input("Enter Attendance:"))
if marks>=35 and attendance>=65:
    print("Pass")
else:
    print("Fail")

#Program-2
marks=int(input("Enter Marks:"))
attendance=int(input("Enter Attendance:"))
if marks>=35 or attendance>=65:
    print("Pass")
else:
    print("Fail")

#Identity Operators
#Program-1
basket1="apple"
basket2="apple"
print(basket1 is basket2)

#Program-2
basket1="apple"
basket2="apple"
print(basket1 is not basket2)

#Program-3
basket1="apple"
basket2=basket1
print(basket1 is basket2)

#Program-4
cart=["book", "pen"]
same_cart=cart
new_cart=["book", "pen"]
print(same_cart is cart)
print(new_cart is cart)

#Membership Operators
Fruits=["apple", "banana", "mango", "watermelon"]
print("watermelon" in Fruits)
print("watermelon" not in Fruits)

#Bitwise Operators
READ=1
WRITE=2
EXECUTE=4
user_permission=READ|WRITE
print("can read:", bool(user_permission and READ))
print("can write:", bool(user_permission and WRITE))
print("can execute:", bool(user_permission and EXECUTE))


