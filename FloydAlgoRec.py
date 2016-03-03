#make this reursive

import sys
file = open('matrix1.txt','r')
m = []
k = (file.read()).split()
#import the data and read it     
for i in k:
    w = i.split(',')
    m = m + [w]
    for x in range(0, (len(w))):
        w[x] = int(w[x])
        if int(w[x]) == 0:
            w[x] = 1000000
        #loop through and replace all occurences of 0 with a large number

y = m
path = []
for i in range(len(m[0])):
	path.append([])
	for j in range(len(m[i])):
		path[i].append(["Node "+str(i)+" goes to "])
a = "node"

sys.setrecursionlimit(100000)#set a limit to the function clals to not break python
def floydRec(m,i,j,k):#recursive function with the parameters
    if (m[i][k] + m[k][j] < m[i][j]):
        m[i][j] = m[i][k] + m[k][j]#same as last week
        path[i][j] += a+str(k)+" to"

    if j < len(m)-1:
        return floydRec(m,i,j+1,k)#when j hasnt ended
    if (j ==(len(m)-1)) & (i < (len(m)-1)):
        return floydRec(m,i+1,0,k)#when j has ended but the i and k havent
    if (i == (len(m)-1)) & (k < (len(m)-1)):#when i and j have ended but k hasnt
        return floydRec(m,0,0,k+1)
    if (i==(len(m)-1)) & (j==(len(m)-1)) & (k==(len(m)-1)):
        return m #when i,j and k have all ended


for i in range(len(m[0])):	
	for j in range(len(m[i])):
		path[i][j] += "node "+str(j)
		


for i in range(0,len(m)):
    m[i][i] = 1000000
#print(y)
print(floydRec(m,0,0,0))#print out recursive funtion,to display the matrix
print(" ")#just a gap...:)
print("shortest distance from 9 to 3 is", m[8][2])#calculate the shortest distances
print("shortest distance from 13 to 14 is", m[12][13])

#m[8][2] --> 172
#m[12][13] --> 114
