#wap to read  the text from a given file "poems.txt" and find out wether it contains the word 'twinkle
f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("the word twinkle is [resent in the content]")
else:
    print("the word twinkle is not prensent int hte content")    

f.close()