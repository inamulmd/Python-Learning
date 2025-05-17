# Print pattern by function
# ***
#**
#*

def pattern(n):
    if(n==0):
        return ""
    print("*"* n)
    pattern(n-1)

f= int(input("enter temperature in F"))
print(pattern(f))