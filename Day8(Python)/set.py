#program-1
set1={1,2,3,4,5}
print(set1)

#program-2
courses=["python", "Java", "C", "SQL"]
unique_courses=set(courses)
print("unique_courses:", unique_courses)

#program-3
student_ids={101, 102, 103, 101, 104}
student_ids.add(105)
print("Add:",student_ids)
student_ids.remove(105)
print("Remove:", student_ids)
print("Length:", len(student_ids))

# add()
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
print("add():", fruits)

# update()
fruits = {"apple", "banana"}
more_fruits = {"mango", "orange"}
fruits.update(more_fruits)
print("update():", fruits)

# remove()
fruits = {"apple", "banana", "mango"}
fruits.remove("banana")
print("remove():", fruits)

# discard()
fruits = {"apple", "banana", "mango"}
fruits.discard("grapes")
print("discard():", fruits)

# pop()
fruits = {"apple", "banana", "mango"}
item = fruits.pop()
print("pop() removed:", item)
print("After pop():", fruits)

# clear()
fruits = {"apple", "banana", "mango"}
fruits.clear()
print("clear():", fruits)

# copy()
fruits = {"apple", "banana", "mango"}
new_fruits = fruits.copy()
print("copy():", new_fruits)

# union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("union():", set1.union(set2))

# intersection()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("intersection():", set1.intersection(set2))

# difference()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
print("difference():", set1.difference(set2))

# symmetric_difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("symmetric_difference():", set1.symmetric_difference(set2))

# intersection_update()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print("intersection_update():", set1)

# difference_update()
set1 = {1, 2, 3, 4}
set2 = {3, 4}
set1.difference_update(set2)
print("difference_update():", set1)

# symmetric_difference_update()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print("symmetric_difference_update():", set1)

# issubset()
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print("issubset():", set1.issubset(set2))

# issuperset()
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print("issuperset():", set1.issuperset(set2))

# isdisjoint()
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print("isdisjoint():", set1.isdisjoint(set2))



