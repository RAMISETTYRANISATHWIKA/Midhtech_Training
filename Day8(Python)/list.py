#Calculate average from marks list
student_marks=[98,99,100]
total=sum(student_marks)
average=total/len(student_marks)
print("Average marks:", average)

#User input
student_marks=list(map(int, input("Enter marks:").split()))
total=sum(student_marks)
average=total / len(student_marks)
print("Average marks:", average)

#List methods

Ramayanam=["Ram", "Sita", "Lakshman","Hanuman"]

#append
list2=Ramayanam.append("Rama")
print(Ramayanam)

# extend 
list2=Ramayanam.extend(["Seetha", "Ayodhya"])
print(Ramayanam)

# insert
Ramayanam.insert(6,"Maruthi")
print(Ramayanam)

# remove
Ramayanam.remove("Maruthi")
print(Ramayanam)

# pop
Ramayanam.pop()
print(Ramayanam)

# clear
list3=[1,2,3,4,5]
list3.clear()
print(list3)

# index
print(Ramayanam[0])

# count
print(Ramayanam.count("Ram"))

# sort
Ramayanam.sort()
print(Ramayanam)

# reverse
Ramayanam.reverse()
print(Ramayanam)

# copy
Sri_Ramayanam=Ramayanam.copy()
print(Sri_Ramayanam)
