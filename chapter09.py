# Tuples are like lists, but immutable
point = (3, 5)
print("Tuple:", point)
print("First element:", point[0])

# Tuples are useful for fixed data
dimensions = (1920, 1080)
print("Screen resolution:", dimensions)

# Tuple unpacking
x, y = point
print("x:", x)
print("y:", y)

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file.\n")
    file.write("Python is writing this content.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)
