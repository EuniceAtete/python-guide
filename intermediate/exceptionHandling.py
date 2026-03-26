# Basic try-except example

print("Basic Try-Except")
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except:
    print("Something went wrong!")
# Specific errors

print("\nESpecific exceptions")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

# Using else

print("Else and Try")

try:
    num = int(input("Enter a number: "))
    result = 10/num
except Exception as err:
    print("Error: ",err) 
else:
    print("The operation was successful.")

#  Multiple exceptions

print("Multiple Exceptions")

try:
    num= int(input("Enter a number: "))
except(ValueError,ZeroDivisionError):
    print("Invalid input or division by zero")

# Raising exceptions
print("\n Manual Raise")

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative!")

print("Your age is:", age)