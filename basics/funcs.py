#USER-DEFINED FUNCTIONS
#No parameters

def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()

#Parameters

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Eunice")

#Return values
def add(a,b):
    return a + b

print(add(9,15))

def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Alice")


#Multiple Parameters


def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person("Eunice", 18)

#Keyword Arguments

describe_person(age=18, name="Eunice")



def multiply(x, y):
    return x * y

print("Multiplication:", multiply(4, 5))
