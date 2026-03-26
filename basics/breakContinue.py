# BREAK AND CONTINUE IN PYTHON

# break → stops the loop completely
# continue → skips current iteration and moves to next one


# Example 1: Using break
print("Example: break")

for i in range(1, 6):
    if i == 4:
        break  # stops the loop when i is 4
    print(i)

# Output:
# 1 2 3


# Example 2: Using continue
print("\nExample: continue")

for i in range(1, 6):
    if i == 3:
        continue  # skip 3
    print(i)

# Output:
# 1 2 4 5


# Example 3: Use break to find a num
print("\nExample: search with break")

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        print("Found 30!")
        break