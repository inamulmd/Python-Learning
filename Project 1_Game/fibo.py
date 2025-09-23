n=int(input("Enter a number: "))

a=0
b=1

for i in range(n+1):
    print(a)
    fibo=a+b
    a=b
    b=fibo
    
