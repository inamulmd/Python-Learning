#wap to print the folllowing star pattern
# * * *
# *   *
# * * *

n = int(input("enter a number"))

for i in range(1, n+1):
     if(i==1 or i==n):
          print("*"* n, end="") #end="" prevent the next line to go
     else:
          print("*", end="")
          print(" "*(n-2), end="")
          print("*", end="") 
          print(" ")       