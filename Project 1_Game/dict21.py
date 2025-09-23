students = {
    "Inamul": 85,
    "Ayesha": 90,
    "Rahul": 78,
    "Sneha": 92,
    "Ali": 88
}

# Step 2: Display all student records
print("📋 All Students and Marks:")
for name, marks in students.items():
    print(f"{name}: {marks}")


# Step 3: Update a student's marks
students["Rahul"] = 83  # updating Rahul's marks
print("\n🔁 Updated Rahul's Marks:")
print("Rahul:", students["Rahul"])

# Step 4: Delete a student's record
del students["Ali"]
print("\n❌ Deleted 'Ali' from records")


# Step 4: Delete a student's record
del students["Ali"]
print("\n❌ Deleted 'Ali' from records")
