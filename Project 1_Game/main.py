import random
'''
1 for Snake
-1 for water
0 for Gun

'''
computer = random.choice([-1, 0, 1])
youstr = input("enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict ={1:"Snake", -1:"Water",0:"Gun"}

you = youDict[youstr]

print(f"you choose {reverseDict[you]}\n Computer choose {reverseDict[computer]}")


if(computer ==you):
    print("it is a draw")
else:    

    if(computer ==-1 and you ==1):
        print("you win!")

    elif(computer ==-1 and you ==0): 
        print("you win!")   

    elif(computer ==1 and you ==-1): 
        print("you loose!")  

    elif(computer ==-1 and you ==0): 
        print("you win!")  

    elif(computer ==0 and you ==1): 
        print("you loss!")  

    elif(computer ==1 and you ==0): 
        print("you win!")  

    else:
        print("somehing went wrong")