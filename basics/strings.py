text = "Hello From Python!"

# Length
print(len(text))  # 18

# Slicing — grabbing a portion of the string THE FIRST INDEX IS INCLUSIVE, THE LAST IS EXCLUSIVE
print(text[0:5])   # Hello
print(text[6:])    # From Python!
print(text[::-1])  # Reverse it!

# Useful methods
print(text.upper())      # HELLO FROM PYTHON!
print(text.lower())      # hello from python!
print(text.title())      # Hello From Python!
print(text.replace("Hello", "Hi"))  # Hi From Python!
print(text.split(" "))   # ['Hello', 'From', 'Python!']

# Check if something is inside
print("Hello" in text)       # True
print("python" not in text)  # True  (case-sensitive!)

# Strip removes extra spaces
messy = "   too much space   "
print(messy.strip())

# Joining two strings
first = "Hello"
last = "World"
print(first + " " + last)  # Hello World