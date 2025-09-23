n = int(input("Enter the number: "))
num=n
temp=n
sum=0
count=0
while(temp):
    count+=1
    temp//=10
   

while(n):
    rem=n%10
    sum= sum + rem **count
    n//=10
if(num==sum):
    print("is armstrong")
else:
    print("Not armstrong")