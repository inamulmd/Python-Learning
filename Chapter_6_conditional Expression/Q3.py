#A apam comment is defined as atext 
p1="Make a lot of Money" 
p2 ="buy now" 
p3 ="subscribe this" 
p4="click this"

message = input("enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("this commmen is not a spam")
    