#Program-1
for i in range(6):
    print(i)

#Program-2
employees=["Ram", "Sita", "Lakshman", "Hanuman"]
for i in employees:
    print(i)


#Program-3
rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of columns:"))
symbol=input("Enter the symbol:")
for i in range(0,rows):
    print(symbol, end="")
    for j in range(0,cols):
        print(symbol, end="")
    print()


#Program-4
#Dail Pad program with digits and * and # 
#Take using 3 tuple sets
digits=(("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"), ("*", "0", "#"))
for i in digits:
    for j in i:
        print(j, end=" ")
    print()