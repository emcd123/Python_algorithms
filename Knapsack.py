#Input
def InputList(string):
    #Pass boolean
    Pass = False
    while(not Pass):
        Pass = True
        #Get list from input
        l = input("Please enter the list of the positive "+string+": ").split(',')
        #Loop through numbers in list
        for val in l:
            val = int(val)
            #If incorrect input pass is false and restart while loop
            if(val <= 0):
                Pass = False
                break
    #Return list
    return l

def Knapsack(v,w,K):
    #Empty matrix
    m = [[]]
    #Make first column all 0
    for i in range(K+1):
        m[0].append(0)
        
    #Loop through 1 to value list +1
    for i in range(1,len(v)+1):
        #Make new row
        m.append([])
        #Loop 0 to Bag capacity+1
        for j in range(K+1):
            if(int(w[i-1]) > j):
                m[i].append(m[i-1][j])
            else:
                m[i].append(max(m[i-1][j],m[i-1][j-int(w[i-1])] + int(v[i-1])))

    #Items to choose
    items = []
    k = K
    i = len(v)
    while(i > 0):
        #If these two are not the same value
        if (m[i][k] != m[i-1][k]):
            #Add i to the list
            items.append(i)
            #Reduce capcacity left in bag
            k = k-int(w[i-1])
        #Decrement i
        i -= 1

    #Print results
    print("Items to pick:",items)
    print("Total value:", m[len(v)][K])

def Main():
    while(True):
        #Input bag capacity
        K = int(input("Please enter the positive bag capacity: "))
        #If K is positive exit loop
        if(K > 0):
            break

    #Empty lists
    values = []
    weights = []
    
    while(True):
        #Input lists
        values = InputList("values")
        weights = InputList("weights")

        #If lists lengths the same
        if(len(values) == len(weights)):
            #Exit loop
            break
        else:
            #Else try again
            print("Two lists must be of the same length")

    #Calculate and output optimal solution
    Knapsack(values,weights,K)
        

Main()

        
