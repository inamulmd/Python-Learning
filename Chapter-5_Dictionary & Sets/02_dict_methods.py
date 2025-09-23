marks = {
    "Harry" : 100,
    "Subham" :56,
    "rohan" :23,
    0: "Harry",
}

# print(marks.items())

print(marks.keys())
# print(marks.values())

marks.update({"Harry": 99, "Renuka": 100})
print(marks.items())

# print(marks.get("harry2")) # Prints None
# print(marks["Harry2"])  #throw an error
