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
"""
1 1 2 1 3 1   
1 2 2 2 3 2   
1 3 2 3 3 3   
1 4 2 4 3 4   
1 5 2 5 3 5 
"""
def pattern_10():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x-1):
            print(j,i,end=" ")
        print("  ")
pattern_10()
"""
1 1 1 2 1 3   
2 1 2 2 2 3   
3 1 3 2 3 3   
4 1 4 2 4 3   
5 1 5 2 5 3 
"""
def pattern_11():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x-1):
            print(i,j,end=" ")
        print("  ")
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
            y = (j + 1) * x - i + 1
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
"""
1       3       5       7       9        
3       5       7       9       11       
5       7       9       11      13       
7       9       11      13      15       
9       11      13      15      17      
"""
def pattern_17():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(0,x):
            print(2*(i+j)-1,end="\t")
        print(" ")
# pattern_17()
"""
0 1 0 1 0  
1 0 1 0 1  
0 1 0 1 0  
1 0 1 0 1  
0 1 0 1 0 
"""
def pattern_18():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if i%2 == 0 and j%2 != 0 or i%2 != 0 and j%2 == 0:  # if (i + j) % 2 != 0:
                print(1,end=" ")
            else:
                print(0,end=" ")
        print(" ")
# pattern_18()
"""
1 0 1 0 1  
0 1 0 1 0  
1 0 1 0 1  
0 1 0 1 0  
1 0 1 0 1  
"""
def pattern_19():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if (i + j) % 2 != 0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        print(" ")
# pattern_19()
"""
1 0 1 0 1  
0 0 0 0 0  
1 0 1 0 1  
0 0 0 0 0  
1 0 1 0 1 
"""
def pattern_20():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if i%2 == 0 or j%2 == 0: 
                print(0,end=" ")
            else:
                print(1,end=" ")
        print(" ")
# pattern_20()
"""
0 1 0 1 0  
0 0 0 0 0  
0 1 0 1 0  
0 0 0 0 0  
0 1 0 1 0
"""
def pattern_21():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if i%2 == 0 or j%2 != 0: 
                print(0,end=" ")
            else:
                print(1,end=" ")
        print(" ")
# pattern_21()
"""
0 0 0 0 0  
1 1 1 1 1  
0 0 0 0 0  
1 1 1 1 1  
0 0 0 0 0 
"""
def pattern_22():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if i%2 == 0 : 
                print(1,end=" ")
            else:
                print(0,end=" ")
        print(" ")
# pattern_22()
"""
1 1 1 1 1  
0 0 0 0 0  
1 1 1 1 1  
0 0 0 0 0  
1 1 1 1 1 
"""
def pattern_23():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if i%2 == 0 : 
                print(0,end=" ")
            else:
                print(1,end=" ")
        print(" ")
# pattern_23()
"""
0 1 0 1 0  
0 1 0 1 0  
0 1 0 1 0  
0 1 0 1 0  
0 1 0 1 0 
"""
def pattern_24():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if j%2 != 0 : 
                print(0,end=" ")
            else:
                print(1,end=" ")
        print(" ")
# pattern_24()
"""
1 0 1 0 1  
1 0 1 0 1  
1 0 1 0 1  
1 0 1 0 1  
1 0 1 0 1 
"""
def pattern_25():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if j%2 == 0 : 
                print(0,end=" ")
            else:
                print(1,end=" ")
        print(" ")
# pattern_25()
"""
A A A A A  
B B B B B  
C C C C C  
D D D D D  
E E E E E  
"""
def pattern_26():
    x = int(input("Enter the number: "))
    for i in range(0,x):
        for j in range(0,x):
            char = chr(65+i)
            print(char,end=" ")
        print(" ")
# pattern_26()

# another way
def another_26():
    x = "ABCDE"
    for i in x:
        for j in x:
            print(i,end=" ")
        print(" ")
another_26()
"""
A B C D E  
A B C D E  
A B C D E  
A B C D E  
A B C D E  
"""
def pattern_27():
    x = int(input("Enter the number: "))
    for i in range(0,x):
        for j in range(0,x):
            char = chr(65+j)
            print(char,end=" ")
        print(" ")
# pattern_27()
"""
E E E E E  
D D D D D  
C C C C C  
B B B B B  
A A A A A  
"""
def pattern_28():
    x = int(input("Enter the number: "))
    for i in range(0,x):
        for j in range(0,x):
            char = chr(69-i)
            print(char,end=" ")
        print(" ")
# pattern_28()
"""
E D C B A  
E D C B A  
E D C B A  
E D C B A  
E D C B A
"""
def pattern_29():
    x = int(input("Enter the number: "))
    for i in range(0,x):
        for j in range(0,x):
            char = chr(69-j)
            print(char,end=" ")
        print(" ")
# pattern_29()
"""
A B C D E  
F G H I J  
K L M N O  
P Q R S T  
U V W X Y 
"""
def pattern_30():
    y=0
    x = int(input("Enter the number: "))
    for i in range(0,x):
        for j in range(0,x):
            char = chr(65+y)
            y +=1
            print(char,end=" ")
        print(" ")
# pattern_30()
"""
A F K P U  
B G L Q V  
C H M R W  
D I N S X  
E J O T Y 
"""
def pattern_31():
    y=0
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(0,x):
            if j%2 == 0:
                y = i+(j*x)
            else:
                y = (j+1)*x-i+1
            char = chr(64+y)
            print(char,end=" ")
        print(" ")
# pattern_31()
"""
A F K P U  
B G L Q V  
C H M R W  
D I N S X  
E J O T Y  
"""
def pattern_32():
    y=0
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(0,x):
            y = i+(j*x)
            char = chr(64+y)
            print(char,end=" ")
        print(" ")
# pattern_32()
"""
E J O T Y  
D I N S X  
C H M R W  
B G L Q V  
A F K P U  
"""
def pattern_33():
    y=0
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(0,x):
            y = (j+1)*x-i+1
            char = chr(64+y)
            print(char,end=" ")
        print(" ")
# pattern_33()
"""
*  
* *  
* * *  
* * * *  
* * * * * 
"""
def pattern_34():
    num = int(input("Enter the number: "))
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i+j > num:
                print('*',end=" ")
        print(" ")
# pattern_34()
"""
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5 
"""
def pattern_35():
    num = int(input("Enter the number: "))
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i+j > num:
                print(i,end=" ")
        print(" ")
# pattern_35()
"""
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5  
"""
def pattern_36():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if i+j >= x+1:
                print((i+j)-x,end=" ")
        print(" ")
# pattern_36()
"""
5  
4 4  
3 3 3  
2 2 2 2  
1 1 1 1 1  
"""
def pattern_37():
    x = int(input("Enter the number: "))
    for i in range(x,0,-1):
        for j in range(x,0,-1):
            if i+j <= x+1:
                print(i,end=" ")
        print(" ")
# pattern_37()
"""
5  
5 4  
5 4 3  
5 4 3 2  
5 4 3 2 1  
"""
def pattern_38():
    x = int(input("Enter the number: "))
    for i in range(x,0,-1):
        for j in range(x,0,-1):
            if i+j <= x+1:
                print((i+j)-1,end=" ")
        print(" ")
# pattern_38()
"""
5  
4 5  
3 4 5  
2 3 4 5  
1 2 3 4 5
"""
def pattern_39():
    x = int(input("Enter the number: "))
    for i in range(x,0,-1):
        for j in range(x,0,-1):
            if i+j <= x+1:
                print((x-j)+1,end=" ")
        print(" ")
# pattern_39()
"""
5  
4 5  
3 4 5  
2 3 4 5  
1 2 3 4 5
"""
def pattern_39B():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if j+i >= x+1:
                print(j,end=" ")
        print(" ")
# pattern_39B()
def pattern_40():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for  j in range(1,x+1):
            if j == i or i == x or j == 1 or i>=j:
                print(i,end=" ")
            else:
                print(" ",end=" ")
            x += 2
        print(" ")
pattern_40()
"""
1  
2 3  
4 5 6  
7 8 9 10 
"""
def pattern_41():
    y = 0
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,x+1):
            if j+i >= x+1:
                y+=1
                print(y,end=" ")
        print(" ")
# pattern_41()
"""
1  
2 3  
3 4 5  
4 5 6 7  
5 6 7 8 9
"""
def pattern_42():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(i,i+i):
                print(j,end=" ")
        print(" ")
# pattern_42()
def pattern_43():
    r = int(input("Enter the number: "))
    for i in range(1,r+1):
        v = i -1
        for j in range(1,i+1):
            print(v+i,end=" ")
            v +=2
        print()
# pattern_43()
"""
1  
3 2  
6 5 4  
10 9 8 7 
"""
def pattern_44():
    x = int(input("Enter the number: "))
    y =0 
    for i in range(1,x+1):
        k = y + i
        for j in range(k,y,-1):
                print(j,end=" ")
                y = k
        print(" ")
# pattern_44()
"""
1  
3 5  
7 9 11  
13 15 17 19  
21 23 25 27 29 
"""
def pattern_45():
    x = int(input("Enter the number: "))
    y =1 
    for i in range(1,x+1):
        for j in range(i):
                print(y,end=" ")
                y += 2
        print(" ")
# pattern_45()
"""
2  
4 6  
8 10 12  
14 16 18 20  
22 24 26 28 30  
"""
def pattern_46():
    x = int(input("Enter the number: "))
    y =2 
    for i in range(1,x+1):
        for j in range(i):
                print(y,end=" ")
                y += 2
        print(" ")
# pattern_46()
"""
1  
2 4  
3 6 9  
4 8 12 16  
5 10 15 20 25
"""
def pattern_47():
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        for j in range(1,i+1):
                print(i*j,end=" ")
        print(" ")
# pattern_47()
def pattern_48():
    Range = int(input("Enter the number: ")) 
    x = y = 1
    z = a = x 
    for i in range(1,Range+1):
        y = z + y 
        for j in range(1,Range+1):
                if i >= j:
                    print(x,end=" ")
                    x = x-a
                    a= a+1
                else:
                    print(" ",end=" ")
        x = y
        z =z -1
        a =z
        print(" ")
pattern_48()
def pattern_50():
    Range = int(input("Enter the range: "))
    for i in range(1,Range+1):
        for j in range(i):
            print("*",end=" ")
        print(" ")
