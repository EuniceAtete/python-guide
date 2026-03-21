#Using for to loop
for i in range(6):
      print(i) #Output is 0,1,2,3,4,5

for i in range(5):
        if i == 3:
            continue #Use of continue to not print the value specified bu tjuss continue with the program
        print(i)#Output is 0,1,2,4
for i in range(5):
      if i == 3:
            break
for i in range(1,6):
      print(i)# Output is 1,2,3,4,5

for i in range(3,12,3):
      print(i) # Output is 3,6,9, First number is the first of the loop, the last exclusive and the steps

for i in range(1,11,2):
      print(i) # Output is 3,6,9