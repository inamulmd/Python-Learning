a= int(input("Enter your age: "))

if(a>=18):
    print("You are the above the age of consent")
    print("Good for you")  

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering ) which is not valid age")
else:
    print("You are below the age of consent")   
     
print("end of Program")     
