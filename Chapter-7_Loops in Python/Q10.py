#wap to  print the multioplication table in revesed

n = int(input("enter a number"))

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")