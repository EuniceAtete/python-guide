i = 1

while i <= 5:
    print(i)
    i += 1  # increase i by 1

# Example 2: User input loop
# Keeps asking until user types 'exit'

command = ""

while command != "exit":
    command = input("Type 'exit' to stop: ")

print("Loop ended")

#ATTENTION

while True:
    print("Oops")  # runs forever