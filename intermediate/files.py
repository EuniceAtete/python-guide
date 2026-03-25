# Creating a file
file = open("file.txt","w")
file.write("Hi. I am Eunice.")
file.close()

print("File written successfully")

# Reading file content

file = open("file.txt","r")
fileContent = file.read()
print("File Content:\n")
print(fileContent)
file.close()

# Appending to a File

file = open("file.txt", "a")
file.write("\nThis line was appended.")
file.close()

print("\nContent appended.")

# Reading Line by Line

with open("example.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())
