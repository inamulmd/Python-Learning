#wap to print the folllowing star pattern
#   *
# * * *
#* *  *  *
 

n = int(input("enter a number"))

for i in range(1,n+1):
    print(" "* (n-i), end="") ## prevent form going o next line
    print("*"*(2*i-1), end="")
    print("") # for new line
