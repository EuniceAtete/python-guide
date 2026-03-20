
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

# Removing Items

student.pop("email")   # Removes by key
print(student)

# Remove last inserted item
student.popitem()
print(student)


# Looping Through a Dictionary

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(key, ":", value)