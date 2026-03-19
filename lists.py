
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
