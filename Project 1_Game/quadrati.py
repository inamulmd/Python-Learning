import cmath  # For complex number support

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
d = cmath.sqrt(b**2 - 4*a*c)

# Calculate the two solutions
x1 = (-b + d) / (2*a)
x2 = (-b - d) / (2*a)

print(f"The solutions are: {x1} and {x2}")
