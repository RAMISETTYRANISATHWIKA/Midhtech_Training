def is_prime(number):
    count=0
    if number<=1:
        print("Prime is not defined for", number)
        return
    for i in range(1, number+1):
        if number%i==0:
            count+=1
    if count==2:
        print("Prime number")
    else:
        print("Not a prime number")
number=int(input("Enter a number:"))
is_prime(number)