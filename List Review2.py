#example3  ####排列组合
# a1 a2 a3 b1 b2 b3 c1 c2 c3
listA = ["a", "b", "c"]
listB = ["1", "2", "3"]
listFinal = []
for a in listA:
        for b in listB:
                listFinal.append(a + b)
for i in listFinal:
    print (i, end="\n")



suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = []  # creates an empty List
for s in suits:
    for v in values:
        deck.append(v + " of " + s)
print (deck)


###
nameList = ["a","b","c","d","e"]
valueList = [11,22,33,44,55]

name = input("name: ")
if name in nameList:
        order = nameList.index(name)
        print(valueList[order])
else:
        print("na")
