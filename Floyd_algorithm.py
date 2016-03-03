file = open('matrix1.txt','r')
m = []
k = (file.read()).split()
    
for i in k:
    w = i.split(',')
    for x in range(0, (len(w))):
        w[x] = int(w[x])
        if w[x] == 0:
            w[x] = 1000000
        
    m = m + [w]

y = m
    
## Finding the shortest distance between two points
## try for 3, 10
     

for k in range(0, len(m)):
    for i in range(0,len(m)):
        for j in range(0, len(m)):
            if (m[i][k] + m[k][j] < m[i][j]):
                m[i][j] = m[i][k] + m[k][j]

for i in range(0,len(m)):
    m[i][i] = 0
print(y)
print(' ')
print("shortest distance from 3 to 10 is", m[2][9])
print("shortest distance from 14 to 9 is", m[13][8])
print("shortest distance from 11 to 5 is", m[10][4])
        
