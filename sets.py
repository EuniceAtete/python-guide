#Creating a set

my_set = {1,2,2,3,4,5}
print(my_set)
#This is gonna print {1,2,3,4} because a set can't have duplicates

# Adding items
my_set.add(5)

# Removing items
my_set.remove(2)

#Traversing through a set

for item in my_set:
    print(item)