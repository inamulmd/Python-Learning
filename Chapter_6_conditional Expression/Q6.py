#wap to calculate the grade of a students from hsi marks
marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    garde = "Ex"
elif(marks<90 and marks>=80):
    garde="A"    
elif(marks<80 and marks>=70):
    garde="B"    
elif(marks<70 and marks>=60):
    garde="C"    
elif(marks<60 and marks>=50):
    garde="D"    
elif(marks<50):
    garde="F"   

print( "Your grade is:", garde)     