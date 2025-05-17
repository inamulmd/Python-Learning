# a file contains a word "Donkey" multiple times . You need to write a program which replace the word with #### ny updating the smae file

word = " Donkey"
with open("file1.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "######")

with open("file1.txt" ,"w") as f:
    f.write(contentNew)   