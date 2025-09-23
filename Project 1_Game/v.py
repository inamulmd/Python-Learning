
def pri(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, num ):
        if(num % i == 0):
            return False

    return True

n=int(input("Ente the number:: "))

for i in range (1,n+1):
    if pri(i):
        print(i, end = ' ')

