#Write a revucrsive function to calculate the sum of first n natural numbers

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) +n


f= int(input("enter temperature in F"))
print(sum(f))