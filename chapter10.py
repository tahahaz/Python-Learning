# Creating a dictionary
students = {
    "Taha": 85,
    "Mujeeb": 90
}

# Adding a new key-value pair
students["Ahmed"] = 78

# Accessing values
print("Marks of Mujeeb:", students["Mujeeb"])

# Iterating over dictionary
for name, marks in students.items():
    print(f"{name} scored {marks} marks")

# Checking if a key exists
if "Taha" in students:
    print("Taha is in the student list.")

# Removing a key
del students["Ahmed"]
print("Updated student list:", students)
