# Taking age input from user
age = int(input("Enter your age: "))

# Using if, elif, else to check conditions
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
