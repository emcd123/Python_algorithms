from sys import exit#import the exit function

weights= input().split(',')#input is taken as a string, turned to lists afterwards
values = input().split(',')
carryCapacity = int(input())#max weight posssible in bag
listWeights = map(int,weights)# create a list of ints out of the weights and value string list
listValues = map(int,values)

if len(listValues) != len(listWeights):
   print("Error:Size of list must be indentical")
   exit()#check for same size,if not same size print error message and exit program

check = all(i>0 for i in listWeights)
check1 = all(k>0 for k in listValues)
if (check == False) and (check1 == False):
    print("Error:All entries in lists must be positive")
    exit()#check all values are greater than 0,if not print error message and exit program

resultList = map(lambda x,y:(x,y),listWeights,listValues)#merge the weight and value lists together into a list of pairs of tuples
#print(resultList)

def powerset(items):#standard function to find the powerset
    resultList = [[]]
    for i in items:
        new = [r+[i] for r in resultList]
        resultList.extend(new)
    return resultList

def knapsack(items,carryCapacity):
    contents = []
    optimalWeight = 0#counters for optimal solution
    highestValue = 0
    for weightValuePair in powerset(items):
        thisWeight = sum([j[0] for j in weightValuePair])#just adding up weights of items
        thisValue = sum([j[1] for j in weightValuePair])#just adding up values of respective items
        if (thisValue > highestValue) and (thisWeight <= carryCapacity):# perform a decision if weight is below max but Ive gotten a new highest value
            highestValue = thisValue#update the counters
            optimalWeight = thisWeight
            knapsack = weightValuePair
    return knapsack, optimalWeight, highestValue#return statements


knapsack, optimalWeight, optimalValue = knapsack(resultList,carryCapacity)
print("Formatted as the contents of the knapsack in list format,then the (optimum weight,highest value) as a tuple :" )
print(optimalWeight, optimalValue)

'''
for capacity of 42: Optimal Weight is 41,Highest Value is 86
for capacity of 71: Optimal Weight is 71, Highest Value is 151
for capacity of 101: Optimal Weight is 101 , Highest Value is 213
'''
