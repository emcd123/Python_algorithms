
def insertionSort(li):#insertion sort function
        for i in range(1,len(li)):
                C = i
                while (C>0) and (li[C] < li[C-1]):
                        li[C], li[C-1] = li[C-1], li[C]
                        C = C-1
        return li
	#directly from previous assignment

def mergesort(list):
	if len(list) < 2:
		return list
	else:
		mp = len(list)//2
		list1 = (list[:mp])
		list2 = (list[mp:])#same as class example till this line
		insertionSort(list1), insertionSort(list2)#calling a sinultaeneous insertion sort function on both lists
		return mergesort(list1),mergesort(list2)#and returning the mergesort


def adapted_sorting(li):
	mp = len(li)//2
	list1 = (li[:mp])#same as in regular mergesort
	list2 = (li[mp:])
	if (len(list1)%2 == 0):##a series of checks to decide whether to insertion sort or merge sort based on even/oddness of len(list)
		return mergesort(li)####WRITE A MODIFIED MERGESORT THAT JUST MERGES BUT DOESNT INSERTION ASWELL
	if (len(list1)%2 != 0):		
		return insertionSort(li)
	if (len(list2)%2 == 0):
		return mergesort(li)
	if (len(list2)%2 != 0):
		return insertionSort(li)
l= [1,3,5,2,9]#a list to use,can be changed as you want
l1= [1,3,5,2,9]
print(mergesort(l))#performing part 1 of this assignment
print(adapted_sorting(l1))#part 2 of this assignment

