import random

li=[]
for i in range(5000):#creating a random list using code from blackboard
	li=li+[random.randrange(-50,50)]

def insertionSort(li):#insertion sort function
        for i in range(1,len(li)):
                C = i
                while (C>0) and (li[C] < li[C-1]):
                        li[C], li[C-1] = li[C-1], li[C]
                        C = C-1
	return li

print(insertionSort(li))



