def student_details(name,course):
    print("student name:", name)
    print("course:", course)
student_details("Ram", "python")
student_details("Sita", "Java")

#prime number using parameters
def is_prime(number):
    count=0
    if number<=1:
        print("Prime is not defined for", number)
        return False
    for i in range(1, number+1):
        if number%i==0:
            count+=1
    if count==2:
        return "prime number"
    else:
        return "not a prime number"
number=int(input("Enter a number:"))
print(is_prime(number))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         