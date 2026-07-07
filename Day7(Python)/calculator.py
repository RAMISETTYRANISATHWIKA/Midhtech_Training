import math
import random
operator=input("Enter operator(+, -, *, /, %, **, //, sqrt, fact, sin, cos, tan, log, ln, sinh, cosh, tanh, cube, exp, 10_power, pi, e, rand):")
if operator in ["+", "-", "*"]:
    if operator=="+":
        n=int(input("Enter how many times you want to perform operations:"))
        result=0
        for i in range(n):
            num=float(input("Enter number:"))
            result+=num
        print(result)

    if operator=="-":
        n=int(input("Enter how many times you want to perform operations:"))
        result=float(input("Enter number:"))
        for i in range(n-1):
            num=float(input("Enter number:"))
            result-=num
        print(result)

    if operator=="*":
        n=int(input("Enter how many times you want to perform operations:"))
        result=1
        for i in range(n):
            num=float(input("Enter number:"))
            result*=num
        print(result)

elif operator in ["/", "%", "**", "//"]:
    num1=float(input("Enter a number:"))
    num2=float(input("Enter a number:"))
    if operator=="/":
        if num2!=0:
                print(num1/num2)
        else:
            print("Cannot divide by zero")
    elif operator=="%":
        if num2!=0:
            print(num1%num2)
        else:
            print("Cannot divide by zero")
    elif operator=="**":
        print(num1**num2)
    elif operator=="//":
        if num2!=0:
            print(num1//num2)
        else:
            print("Cannot divide by zero")
elif operator=="sqrt":
    num=float(input("Enter a number:"))
    if num>=0:
        print(math.sqrt(num))
    else:
        print("Square root of a negative number is not possible")
elif operator=="fact":
    num=int(input("Enter a number:"))
    if num>=0:
        print(math.factorial(num))
    else:
        print("Factorial of a negative number is not possible")
elif operator=="sin":
    num=float(input("Enter angle in degrees:"))
    print(math.sin(math.radians(num)))
elif operator=="cos":
    num=float(input("Enter angle in degrees:"))
    print(math.cos(math.radians(num)))
elif operator=="tan":
    num=float(input("Enter angle in degrees:"))
    print(math.tan(math.radians(num)))
elif operator=="sinh":
    num=float(input("Enter a number: "))
    print(math.sinh(num))
elif operator=="cosh":
    num=float(input("Enter a number: "))
    print(math.cosh(num))
elif operator=="tanh":
    num=float(input("Enter a number: "))
    print(math.tanh(num))
elif operator=="log":
    num=float(input("Enter a number:"))
    if num>0:
        print(math.log10(num))
    else:
        print("log is not defined for zero or negative numbers")
elif operator=="ln":
    num=float(input("Enter a number:"))
    if num>0:
        print(math.log(num))
    else:
        print("ln is not defined for zero or negative numbers") 
elif operator=="cube":
    num=float(input("Enter a number:"))
    if num>=0:
        print(num**(1/3))
    else:
        print(-((-num)**(1/3)))
elif operator=="exp":
    num=float(input("Enter a number:"))
    print(math.exp(num))
elif operator=="10_power":
    num=float(input("Enter a number:"))
    print(10**num)
elif operator=="pi":
    print(math.pi)
elif operator=="e":
    print(math.e)
elif operator=="rand":
    print(random.random())
else:
    print("Invalid Operator")
