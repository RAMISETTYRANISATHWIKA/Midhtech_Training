#Before 3.7 version, they are unordred and after 3.7, the dictioaries are ordered

# program-1
student={"name": ["Ram", "Sita", "Lakshman", "Hanuman"], 
         "marks":[100,100,100,100]}
print(student)

# program-2
student_record={"name":"Ram", "marks":99}
student_record["marks"]=100
student_record["grade"]="A+"
print("student_record:", student_record)

# program-3
employee_details={"id":101, "name":"Ram", "dept":"IT", "Salary":100000}
print("Employee Name:",employee_details["name"])
employee_details["city"]="Hyd"
employee_details["Salary"]=1000000
print(employee_details)


# clear()
student = {"name": "Ram", "age": 21, "course": "Python"}
student.clear()
print("clear():", student)

# copy()
student = {"name": "Ram", "age": 21, "course": "Python"}
new_student = student.copy()
print("copy():", new_student)

# fromkeys()
keys = ["name", "age", "course"]
new_dict = dict.fromkeys(keys, "Not Available")
print("fromkeys():", new_dict)

# get()
student = {"name": "Ram", "age": 21, "course": "Python"}
print("get():", student.get("name"))

# items()
student = {"name": "Ram", "age": 21, "course": "Python"}
print("items():", student.items())

# keys()
student = {"name": "Ram", "age": 21, "course": "Python"}
print("keys():", student.keys())

# values()
student = {"name": "Ram", "age": 21, "course": "Python"}
print("values():", student.values())

# pop()
student = {"name": "Ram", "age": 21, "course": "Python"}
student.pop("age")
print("pop():", student)

# popitem()
student = {"name": "Ram", "age": 21, "course": "Python"}
student.popitem()
print("popitem():", student)

# setdefault()
student = {"name": "Ram", "age": 21}
student.setdefault("course", "Python")
print("setdefault():", student)

# update()
student = {"name": "Ram", "age": 21}
student.update({"course": "Python", "city": "Hyderabad"})
print("update():", student)