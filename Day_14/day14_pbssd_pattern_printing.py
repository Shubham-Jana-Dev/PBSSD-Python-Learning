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
# Class Work 
"""
5       10      15      20      25       
30      35      40      45      50       
55      60      65      70      75       
80      85      90      95      100      
105     110     115     120     125 
"""
"""
ran = int(input("Enter the size of Matrix: "))
x = 5
for i in range(1,ran+1):
    for j in range(1,ran+1):
        print(x," ",end="\t")
        x += 5
    print(" ")
"""
# 
'''
1 1              
2 1     2 2            
3 1     3 2     3 3          
4 1     4 2     4 3     4 4        
5 1     5 2     5 3     5 4     5 5 
'''
'''
ran = int(input("Enter the range: "))
for i in range(1,ran+1):
    for j in range(1,ran+1):
        if i>=j:
            print(i,j," ",end="\t")
        else:
            print(" ",end=" ")
    print(" ")
'''
# 
"""
                                1 5      
                        2 4     2 5      
                3 3     3 4     3 5      
        4 2     4 3     4 4     4 5      
5 1     5 2     5 3     5 4     5 5 
"""
"""
rna = int(input("Enter the range: "))
for i in range(1,rna+1):
    for j in range(1,rna+1):
        if i+j >= rna +1:
            print(i,j," ",end="\t")
        else:
            print(" ",end="\t")
    print(" ")
"""
# 
"""
1 1     1 2     1 3     1 4     1 5      
2 1     2 2     2 3     2 4              
3 1     3 2     3 3                      
4 1     4 2                              
5 1                                  
"""
"""
rna = int(input("Enter the range: "))
for i in range(1,rna+1):
    for j in range(1,rna+1):
        if i+j <= rna +1:
            print(i,j," ",end="\t")
        else:
            print(" ",end="\t")
    print(" ")
"""
#
'''
1 1     1 2     1 3     1 4     1 5      
        2 2     2 3     2 4     2 5      
                3 3     3 4     3 5      
                        4 4     4 5      
                                5 5   
'''
'''
rna = int(input("Enter the range: "))
for i in range(1,rna+1):
    for j in range(1,rna+1):
        if i <= j:
            print(i,j," ",end="\t")
        else:
            print(" ",end="\t")
    print(" ")
'''
#
"""
1 1     1 2     1 3     1 4     1 5      
        2 2                     2 5      
                3 3             3 5      
                        4 4     4 5      
                                5 5 
"""
"""
rna = int(input("Enter the range: "))
for i in range(1,rna+1):
    for j in range(1,rna+1):
        if i == j or i ==1 or j == rna:
            print(i,j," ",end="\t")
        else:
            print(" ",end="\t")
    print(" ")
"""
#
'''
1 1     1 2     1 3     1 4     1 5      
2 1     2 2                     2 5      
3 1             3 3             3 5      
4 1                     4 4     4 5      
5 1     5 2     5 3     5 4     5 5 
'''
'''
Range = int(input("Enter the range: "))
for i in range(1,Range+1):
    for j in range(1,Range+1):
        if i == j or i ==1 or j == 1 or i == Range or j == Range:
            print(i,j," ",end="\t")
        else:
            print(" ",end="\t")
    print(" ")
'''
#
"""
1 1     1 2     1 3     1 4     1 5     1 6     1 7     1 8     1 9     1 10     
2 1     2 2                                                     2 9     2 10     
3 1             3 3                                     3 8             3 10     
4 1                     4 4                     4 7                     4 10     
5 1                             5 5     5 6                             5 10     
6 1                             6 5     6 6                             6 10     
7 1                     7 4                     7 7                     7 10     
8 1             8 3                                     8 8             8 10     
9 1     9 2                                                     9 9     9 10     
10 1    10 2    10 3    10 4    10 5    10 6    10 7    10 8    10 9    10 10 
"""
"""
Range = int(input("Enter the range: "))
for i in range(1,Range+1):
    for j in range(1,Range+1):
        if (i == j) or (j+i == Range+1) or (i == 1) or (j == 1) or (i == Range) or (j == Range):
            print(i,j," ",end="\t")
        else:
            print(" ",end="\t")
    print(" ")
"""
#
'''
1 1                                      
2 1     2 2                              
3 1             3 3                      
4 1                     4 4              
5 1     5 2     5 3     5 4     5 5
'''
'''
Rg = int(input("Enter the range: "))
for i in range(1,Rg+1):
    for j in range(1,Rg+1):
        if j == 1 or  i == j or i == Rg: 
            print(i,j," ",end="\t")
        else:
            print(" ",end="\t")
    print(" ")
'''
#
"""
                1 3                      
                2 3                      
3 1     3 2     3 3     3 4     3 5      
                4 3                      
                5 3                  
"""
"""
Rg = int(input("Enter the range: "))
for i in range(1,Rg+1):
    for j in range(1,Rg+1):
        if i == (Rg+1)/2 or j == (Rg+1)/2:
            print(i,j," ",end="\t")
        else:
            
            print(" ",end="\t")
    print(" ")
"""
#
'''
1 1                                     1 6                                     1 11     
        2 2                             2 6                             2 10             
                3 3                     3 6                     3 9                      
                        4 4             4 6             4 8                              
                                5 5     5 6     5 7                                      
6 1     6 2     6 3     6 4     6 5     6 6     6 7     6 8     6 9     6 10    6 11     
                                7 5     7 6     7 7                                      
                        8 4             8 6             8 8                              
                9 3                     9 6                     9 9                      
        10 2                            10 6                            10 10            
11 1                                    11 6                                    11 11    

'''
'''
gg = int(input("Enter the range (Odd number plz): "))
for i in range(1,gg+1):
    for j in range(1,gg+1):
        if j==i or i+j == gg+1 or j == (gg+1)/2 or i == (gg+1)/2:
            print(i,j," ",end="\t")
        else:
            print(" ",end="\t")
    print(" ")
'''