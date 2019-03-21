#POP
#pop up and delete
sampleList1 = ["a","b","c"]
samplePop = sampleList1.pop(-1)
print (samplePop)
for i in sampleList1:
    print (i, end=" ")

#INDEX
#order in the list
sampleList2 = ["a","b","c"]
sampleIndex = sampleList2.index("b")
print (sampleIndex)


#COUNT
#count the total amount of the same item in a list
sampleList3 = ["a","b","c","a","a"]
sampleCount = sampleList3.count("a")
print (sampleCount)


#reverse
sampleList4 = ["a","b","c"]
sampleList4.reverse()
print (sampleList4)
#for i in sampleList4:
    #print (i, end=" ")


#SORT
#only for int
sampleList = [3,5,4,1,2]
sampleList.sort()
print (sampleList)
sampleList.sort(reverse = True)
print (sampleList)
