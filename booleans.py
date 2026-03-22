print(5 > 3)
print(10 == 5)
print(7 != 7)
print(4 <= 9)
print(6 >= 6)

#Using and & or with booleans

x = 10
y = 5

print(x > 5 and y < 10)
print(x < 5 or y < 10)
print(not(x > 5))

#Real-life use of booleans
#Vote process
age = 20

if age >= 18:
    print("You can vote")

#Authentication

password = "abc123"

if password == "abc123":
    print("Access granted")
else:
    print("Access denied")


d = True
e = False
z = None

print(d, e, z)

# Boolean in conditions
if d:
    print("d is True")