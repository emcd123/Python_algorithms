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

def Knapsack(v,w,c,K):
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
            #Append current as last
            m[i].append(m[i-1][j])
            #Loop from 1 to number of items i-1
            for k in range(1,int(c[i-1])+1):
                #If k * weight of i-1 > j then leave loop
                if(k*int(w[i-1]) > j):
                   break
                value = m[i-1][j-k*int(w[i-1])] + k*int(v[i-1])
                #If value is greater than current entry, entry is value
                if(value > m[i][j]):
                    m[i][j] = value
    #Empty list of what to choose
    s = []

    #i = number of items
    i = len(v)
    #j = weight of bag
    j = K
    #Add 0 to s for each item
    for l in range(len(v)):
        s.append(0)
    #Loop through i from number of items to 0
    while(i >= 0):
        val = m[i][j]
        k = 0
        while(not val == m[i-1][j] + k * int(v[i-1])):
            #Decrement j by weight of i-1
            j -= int(w[i-1])
            #Leave loop
            if(j < 0):
                break
            #Increment item and k
            s[i-1] += 1
            k += 1
        #Decrement i
        i -= 1

    #Calculate total optimal value
    total = 0
    for i in range(len(s)):
        #total += number of item i * value of i
        total += int(s[i])*int(v[i]) 
        
    #Print results
    print("Number of items to pick:",s)
    print("Total value:", total)

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
    counts = []
                                 
    while(True):
        #Input lists
        values = InputList("values")
        weights = InputList("weights")
        counts = InputList("counts")

        #If lists lengths the same
        if(len(values) == len(weights) and len(weights) == len(counts)):
            #Exit loop
            break
        else:
            #Else try again
            print("Two lists must be of the same length")

    #Calculate and output optimal solution
    Knapsack(values,weights,counts,K)
        

Main()

#50kg
"""Number of items to pick: [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0]
Total value: 100"""
#80kg
""""Number of items to pick: [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 3]
Total value: 163"""
#110kg
"""Number of items to pick: [0, 0, 0, 0, 0, 1, 2, 0, 0, 1, 0, 2]
Total value: 222"""

        
