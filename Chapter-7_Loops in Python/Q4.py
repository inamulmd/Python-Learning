#wap to find wethewr a given number is primne or not

n = int(input("enter a number"))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")    