"""
* * * * *  
* * * * *  
* * * * *  
* * * * *  
* * * * *  
"""
def pattern_01():
    num = int(input("Enter the number: "))
    for i in range(1,num+1):
        for j in range(1,num+1):
            print("*",end=" ")
        print(" ")
# pattern_01()
"""
1 1 1 1 1  
2 2 2 2 2  
3 3 3 3 3  
4 4 4 4 4  
5 5 5 5 5 
"""
def pattern_02():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(i,end=" ")
        print(" ")
# pattern_02()
"""
1 2 3 4 5  
1 2 3 4 5  
1 2 3 4 5  
1 2 3 4 5  
1 2 3 4 5  
"""
def pattern_03():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(j,end=" ")
        print(" ")
# pattern_03()
"""
5 5 5 5 5  
4 4 4 4 4  
3 3 3 3 3  
2 2 2 2 2  
1 1 1 1 1 
"""
def pattern_04():
    x = int(input("Enter the number: "))
    for i in range(x,0,-1):
        for j in range(x,0,-1):
            print(i,end=" ")
        print(" ")
# pattern_04()
"""
5 4 3 2 1  
5 4 3 2 1  
5 4 3 2 1  
5 4 3 2 1  
5 4 3 2 1  
"""
def pattern_05():
    x = int(input("Enter the number: "))
    for i in range(x,0,-1):
        for j in range(x,0,-1):
            print(j,end=" ")
        print(" ")
# pattern_05()
"""
1       2       3       4       5        
6       7       8       9       10       
11      12      13      14      15       
16      17      18      19      20       
21      22      23      24      25   
"""
def pattern_06():
    y = 1
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(y,end="\t")
            y +=1
        print(" ")
# pattern_06()
"""
1       3       5       7       9        
11      13      15      17      19       
21      23      25      27      29       
31      33      35      37      39       
41      43      45      47      49  
"""
def pattern_07():
    y = 1
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(y,end="\t")
            y +=2
        print(" ")
# pattern_07()
"""
2       4       6       8       10       
12      14      16      18      20       
22      24      26      28      30       
32      34      36      38      40       
42      44      46      48      50
"""
def pattern_08():
    y = 2
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(y,end="\t")
            y +=2
        print(" ")
# pattern_08()
"""
1       2       3       4       5         
2       4       6       8       10        
3       6       9       12      15        
4       8       12      16      20        
5       10      15      20      25  
"""
def pattern_09():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(i*j,end="\t")
        print("  ")
# pattern_09()

# pattern_10()
# pattern_11()

"""
1       6       11      16      21       
2       7       12      17      22       
3       8       13      18      23       
4       9       14      19      24       
5       10      15      20      25  
"""
def pattern_12():
    y = 0
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(0,x):
            y =i+(j*x)
            print(y,end="\t")
        print(" ")
# pattern_12()
"""
1       10      11      20      21       
2       9       12      19      22       
3       8       13      18      23       
4       7       14      17      24       
5       6       15      16      25 
"""
def pattern_13():
    y = 0
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(0,x):
            if j%2 != 0:
                y = (j + 1) * x - i + 1
            else:
                y =i+(j*x)
            print(y,end="\t")
        print(" ")
# pattern_13()
"""
5       10      15      20      25       
4       9       14      19      24       
3       8       13      18      23       
2       7       12      17      22       
1       6       11      16      21   
"""
def pattern_14():
    y = 0
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(0,x):
            y = (j+ 1)* x - i + 1
            print(y,end="\t")
        print(" ")
# pattern_14()
"""
5       6       15      16      25       
4       7       14      17      24       
3       8       13      18      23       
2       9       12      19      22       
1       10      11      20      21   
"""
def pattern_15():
    y = 0
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(0,x):
            if j%2 == 0:
                y = (j + 1) * x - i + 1
            else:
                y =i+(j*x)
            print(y,end="\t")
        print(" ")
# pattern_15()
"""
1       2       3       4       5        
2       3       4       5       6        
3       4       5       6       7        
4       5       6       7       8        
5       6       7       8       9  
"""
def pattern_16():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(0,x):
            print(i+j,end="\t")
        print(" ")
# pattern_16()
def pattern_17():
    y = 0
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(0,x):
            print(2*(i+j)-1,end="\t")
        print(" ")
pattern_17()




