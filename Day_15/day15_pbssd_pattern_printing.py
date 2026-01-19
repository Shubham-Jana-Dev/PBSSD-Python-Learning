"""
*       *  
* *     *  
*   *   *  
*     * *  
*       *  
"""
"""
Rg = int(input("Enter the range: "))
for i in range(1,Rg+1):
    for j in range(1,Rg+1):
        if j == Rg or j == 1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
"""
#################################################################################################################
'''
*       *  
*     * *  
*   *   *  
* *     *  
*       * 
'''
'''
Rg = int(input("Enter the range: "))
for i in range(1,Rg+1):
    for j in range(1,Rg+1):
        if j == Rg or j == 1 or j+i==Rg+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
'''
#################################################################################################################
"""
* * * * *  
      *    
    *      
  *        
* * * * * 
"""
"""
Rg = int(input("Enter the range: "))
for i in range(1,Rg+1):
    for j in range(1,Rg+1):
        if i == Rg or i == 1 or j+i==Rg+1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
"""
#################################################################################################################
'''
*       *  
* *   * *  
*   *   *  
* *   * *  
*       * 
'''
'''
h = int(input("Enter the range: "))
for i in range(1,h+1):
    for j in range(1,h+1):
        if j == 1 or j == h or i+j == h+1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print(" ")
'''
#################################################################################################################
"""
* * * * *  
  *   *    
    *      
  *   *    
* * * * *
"""
"""
t = int(input("Enter the range: "))
for i in range(1,t+1):
    for j in range(1,t+1):
        if j == i or i == 1 or i+j == t+1 or i == t:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
"""
