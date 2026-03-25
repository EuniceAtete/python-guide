# "and" — both must be True
print(True and True)   # True
print(True and False)  # False

# "or" — at least one must be True
print(True or False)   # True
print(False or False)  # False

# "not" — flips it
print(not True)   # False
print(not False)  # True

# Real use case:
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter.")