
#Creating a List

numbers = [1, 2, 3, 4, 5]
names = ["Eunice", "Alice", "Bob"]

print(numbers)
print(names)



# 2. Accessing List Items (Indexing)

# Index starts at 0
print(numbers[0])   # First item
print(numbers[2])   # Third item

# Negative indexing (from the end)
print(numbers[-1])  # Last item

# Changing List Items

numbers[0] = 10
print(numbers)

#Adding items

numbers.append(6)   # Add to end
print(numbers)

numbers.insert(1, 99)  # Insert at position
print(numbers)

#Removing items

numbers.remove(99)  # Remove specific value
print(numbers)

numbers.pop()       # Remove last item
print(numbers)


# Looping Through a List


for num in numbers:
    print(num)



# List Length


print("Length:", len(numbers))



# Checking if Item Exists

if 3 in numbers:
    print("3 is in the list")

# Combining Lists

list1 = [1, 2]
list2 = [3, 4]

combined = list1 + list2
print(combined)