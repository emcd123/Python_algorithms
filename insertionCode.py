import random

#creating a random list using random module,and performing a list comprehension on it
#Couldnt find a way of not using a range so I just picked a reasonbly large number as the upper limit since the size of the list 
#is all that matters and its speed
#li = [random.randrange(1,10000) for c in range(0,10)]
#insertItem = 10000

#http://www.maths.nuigalway.ie/
#~gettrick/teach/cs102/
li=[]
for i in range(600):
  li=li+[random.randrange(-50,50)]
#print li


def nonBinaryInsert(li,item):
#create a function to insert an element into a list, without using binary insert
	i = len(li)-1 #take len of the used list and minus one to subtract our own inserted element
	li = li+[item] #appened our element to end of list so we can begin soting

	while(i>= 0 and item<li[i]):
		li[i+1]=li[i]
		i = i-1
		li[i+1]=item
	return li
	
def insertSort(li):
	#takes a randomly generated lsit,loop through it and sorts it
	for c in range(1,len(li)):
		current = li[c]
		C = c-1		

		while(C>=0) and (li[C]>current):
			li[C+1] = li[C]
			C = C-1
	li[C+1] = current
	return li
#print(nonBinaryInsert(randList,insertItem))

def insertionSort(li):#this is the sorting algorithm that works
	for i in range(1,len(li)):
		C = i
		while (C>0) and (li[C] < li[C-1]):
			li[C], li[C-1] = li[C-1], li[C]
			C = C-1 
	return li
list1 = [1,3,4,2,5,8,100,200,150,123,6]
print(insertionSort(li))

