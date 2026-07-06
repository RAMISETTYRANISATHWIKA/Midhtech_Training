#Program-1
#if
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
num3=int(input("Enter number:"))
maximum=max(num1, num2, num3)
minimum=min(num1, num2, num3)
print(f"The maximum of {num1}, {num2} and {num3} is {maximum}")
print(f"The minimum of {num1}, {num2} and {num3} is {minimum}")


#Program-2
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
num3=int(input("Enter number:"))
if num1>=num2 and num1>=num3:
    print(f"{num1} is the highest")
elif num2>=num1 and num2>=num3:
    print(f"{num2} is the highest")
else:
    print(f"{num3} is the highest")

