# f= open("file.txt")
# print(f.open())
# f.close()

# the same can be written using with statement like this
with open("file.txt") as f:
    print(f.read())  

# You dont have to explicity close the file    