'''
1 1     1 2     1 3     1 4     1 5      
2 1     2 2     2 3     2 4     2 5      
3 1     3 2     3 3     3 4     3 5      
4 1     4 2     4 3     4 4     4 5      
5 1     5 2     5 3     5 4     5 5 
'''
'''
rg = int(input("Enter the of the matrix: "))
for i in range(1,rg+1):
    for j in range(1,rg+1):
        print(i,j," ",end="\t")
    print(" ")
'''
"""
1       2       3       4       5        
2       4       6       8       10       
3       6       9       12      15       
4       8       12      16      20       
5       10      15      20      25  
"""
"""
rg = int(input("Enter the size of the matrix: "))
for i in range(1,rg+1):
    for j in range(1,rg+1):
        print(j*i," ",end="\t")
    print(" ")
"""
'''
2   3   4   5   6    
3   4   5   6   7    
4   5   6   7   8    
5   6   7   8   9    
6   7   8   9   10
'''
'''
rg = int(input("Enter the size of the matrix: "))
for i in range(1,rg+1):
    for j in range(1,rg+1):
        print(i+j," ",end="\t")
    print(" ")
'''
"""
1       2       3       4       5        
6       7       8       9       10       
11      12      13      14      15       
16      17      18      19      20       
21      22      23      24      25 
"""
"""
rg = int(input("Enter the size of the matrix: "))
count = 1
for i in range(1,rg+1):
    for j in range(1,rg+1):
        print(count," ",end="\t")
        count+=1
    print(" ")
"""
#rg = int(input("Enter the size of the matrix: "))
'''
1       6       11      16      21       
2       7       12      17      22       
3       8       13      18      23       
4       9       14      19      24       
5       10      15      20      25 
'''
'''
rg = 5
count = 1
for i in range(1,rg+1): 
    for j in range(0,rg):
        count = i+(j*rg)
        print(count," ",end="\t") 
    print(" ")
'''
# found a number from a matrix
"""
1       6       11      16      21       
2       7       12      17      22       
3       8       13      18      23       
4       9       14      19      24       
5       10      15      20      25       
23 found :)
"""
"""
rg = 5
count = 1
terget = 23
found = 0
for i in range(1,rg+1): 
    for j in range(0,rg):
        count = i+(j*rg)
        print(count," ",end="\t") 
        if count == terget:
            found =1
    print(" ")
if found == 1:
    print("23 found :)")
else:
    print("23 not found :(")
"""
# found a number with it's Coordination
'''
1       6       11      16      21       
2       7       12      17      22       
3       8       13      18      23       
4       9       14      19      24       
5       10      15      20      25       
23  has found at i = 3 y= 5  :)
'''
'''
rg = 5
count = 0
terget = 23
x = 0
y = 0
found = 0
for i in range(1,rg+1):
    for j in range(0,rg):
        count = i+(j*rg)
        print(count," ",end="\t")
        if(count == terget):
            found = 1
            x = i
            y = j +1
    print(" ")
if found == 1:
    print(terget," has found at i =",x,"y=",y ," :)")
else:
    print(terget," not found. :(")
'''

'''
1   1   1   1   1    
2   2   2   2   2    
3   3   3   3   3    
4   4   4   4   4    
5   5   5   5   5 
'''
'''
Range = int(input("Enter the range: "))
for i in range(1,Range+1):
    for j in range(1,Range+1):
        print(i," ",end=" ")
    print(" ")
'''