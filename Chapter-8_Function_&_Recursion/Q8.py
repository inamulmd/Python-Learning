#wap to remove a given word from a list and strip it at the same time
def rem(l, word):
    n=[]
    for item in l: #l.remove(word )
        if not(item == word):
            n.append(item.strip(word))
    return n




l = ["harry", "Rohan", "Subham", "an"]

print(rem(l ,"an"))