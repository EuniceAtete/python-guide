
# Creating a Dictionary

student = {
    "name": "Jenny",
    "age": 16,
    "course": "Software Programming and Embedded Systems"
}

print(student)


# Accessing Values

print(student["name"])
print(student["age"])

# Using get()
print(student.get("course"))

# Changing Values

student["age"] = 19
print(student)

# Adding New Items

student["email"] = "eunice@example.com"
print(student)