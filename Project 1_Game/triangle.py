a=int(input("Enter the first side of the triangle: "))
b=int(input("Enter the first side of the triangle: "))
c=int(input("Enter the first side of the triangle: "))

s= (a+b+c)/2
area =(s*(s-a)*(s-b)*(s-c))**0.5
print(f"The area of the triangle is: {area}")