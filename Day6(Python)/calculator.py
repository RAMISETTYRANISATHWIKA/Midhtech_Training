operator=input("Enter operator(+, -, *, /, %):")
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
elif operator=="%":
    print(num1%num2)
else:
    print("Invalid Operator")