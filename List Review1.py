sampleList = [1,2,3,4,5,6]
#print all items without brackets
for i in sampleList:
    print (i, end="\t")

#print all items in different lines
for i in sampleList:
    print (i, end="\n")

#change items
sampleList[2:3] = [0,0]
print (sampleList)

#adding items
sampleList.append(7)
sampleList = sampleList + [8]
sampleList += [9]
sampleList += [10,11,12]
print (sampleList)
#removing items
del sampleList[-1]
print (sampleList)
del sampleList[2:4]
print (sampleList)


#example1
marks = [0, 1, 2, 3, 4, 5, 6, 7, 8]
total = 0

for mark in marks:
    total += mark

average =total / len(marks)
print(len(marks)) #number of items in the list: len(list)
print ("Average : ", average)


#example2
"""INDEX"""
classes = ["CHC2P", "CHV2OH", "ENG2DN", "GLC2OH", "ICS3M","MPM2D", "SNC21", "SNC2D", "HFN2O"]
marks = [87, 76, 74, 83, 88, 79, 92, 65, 78]

course = input("What class do you want the mark for?")
if course in classes:  #if the input is in the list
    spot = classes.index(course)   #list.index(item)  --the order of item in the list
    #print(spot)
    print ("Your mark in", course, "is", marks[spot])
else:
    print ("You don't have", course)


