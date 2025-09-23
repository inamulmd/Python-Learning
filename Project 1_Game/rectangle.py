def area(length, width):
    return length * width

# Positional arguments
print("Area (Positional):", area(10, 5))  # 10 is length, 5 is width



def area1(length, width):
    return length * width

# Keyword arguments
print("Area (Keyword):", area1(length=8, width=4))
print("Area (Keyword - different order):", area1(width=4, length=8))
