print("Hello, World!")

name = "Eunice"
age = 15

# f-strings let you plug variables right into text
print(f"My name is {name} and I am {age} years old.")

# You can also format numbers
price = 6.99
print(f"The price is {price:.2f}")  # .2f = 2 decimal places


#Printing with two statements on separate lines using one line of code

print("My name is Eunice.");print("Nice to meet you!!")

print("Hello","Git!") # There is a space in between by default

#String concatenation
print("Hello","from","Python","World!") #A space between each statement on one line
print("Hello"+"from"+"Python"+ "World!") #No space between them

#Strings, variables and numbers in one string

name = "Jenny"
age = 16
print("Hi",name,"!")

print("I am",name,"and I am",age,"years old!")
print(f"My name is {name} and I am {age}")
#Length of the string

print(len(name))

#Inclusion and Exclusion of a string in a string

print("nny" in name)
print("me" in name)

#Slicing Strings

print(name[0:5]) #From index 0 to 5
print(name[:4]) #From the start index to 4
print(name[6:]) # From 6 to the end
print(name[-7:-1]) # From the back, -1 is the last index
print(name[::-1]) #Reverse string

#Modification of strings

print(name.upper())
print(name.lower())

string = "     Muahaha"

print(string)
print(string.strip())


print(string.replace("M","H"))

#Escape Characters

print('She said: "I was mad"') #USING DIFFERENT QUOTES

# \', \", \\, \n, \b, \t, \a

print("I am\nEunice")
print("I deleted the last\b")
print("\a I may make a sound")
print("\"My dog is whaaat\"")
print('It\'s just another normal day')

#Methods

print(string.upper())
print(string.lower)
print(string.casefold())#lower but stronger
print(string.title())
print(string.istitle())#Starts with capital
string3 = 5
print(string3.zfill())# Add zeros ar the beginning

