# String declaration and basic operations
message = "Python is fun"
print(message)
print("Length:", len(message))

# Accessing characters
print("First character:", message[0])
print("Last character:", message[-1])

# String slicing
print("Slice [0:6]:", message[0:6])

# Changing case
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())

# String concatenation
greeting = "Hello"
name = "Taha"
print(greeting + ", " + name + "!")

# String formatting
formatted = f"{greeting}, {name}! Welcome to Python."
print(formatted)
