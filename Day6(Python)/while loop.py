#Program-1
count=10
while count>=0:
    print(count)
    count-=1

#Program-2
count=1
while count<=10:
    print(count)
    count+=1

#Program-3
food=input("Enter your food item(Press q to quit):")
while food!="q":
    print(f"You like {food}")
    food=input("Enter your food item(Press q to quit):")
print("Thank You")
rating=int(input("Enter Rating between 1-10:"))
while rating <1 or rating>10:
    print("Invalid number")
    rating=input("Enter Rating between 1-10:")
print(f"you have given {rating} rating to the food")







