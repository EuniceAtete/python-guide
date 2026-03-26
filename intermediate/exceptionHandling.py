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