#Wap to find out whether a file is identical & matches the content of another file
with open("file3.txt") as f:
    content1 = f.read()

with open("file2.txt") as f:
    content2 = f.read()

if(content1 ==content2):
    print("yes these files are identical")
else:
    print("Nod these files are not identicals")    