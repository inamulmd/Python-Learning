#Wap to find out wwether a student has passed or failed if it required a tottal of 40%marks and atleast 33% in each subject to pass.
# assume 3 subject and take marks as an input from the user

marks1 = int(input("enter marks 1: "))
marks2 = int(input("enter marks 3: "))
marks3 = int(input("enter marks 3: "))

#check for total percentage
total_per = (100*(marks1 + marks2+marks3))/300

if(total_per>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass",total_per)
else:
    print("You faiked , try again next years!",total_per)    