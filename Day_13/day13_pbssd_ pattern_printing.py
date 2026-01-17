"""
* * * *  
* * * *  
* * * *  
* * * * 
"""
#--------------------------------------------------------------------
"""
r = int(input("Enter the Range: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        print("*",end=" ")
    print(" ")
"""
#####################################################################
"""
*          
* *        
* * *      
* * * *    
* * * * *
"""
#--------------------------------------------------------------------
"""
r = int(input("Enter the Range: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if i >=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
"""
#####################################################################
'''
        *  
      * *  
    * * *  
  * * * *  
* * * * *  
'''
#--------------------------------------------------------------------
'''
r = int(input("Enter the Range: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if  i+j >= r+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
'''
#####################################################################
"""
* * * * *  
  * * * *  
    * * *  
      * *  
        *  
"""
#--------------------------------------------------------------------
"""
r = int(input("Enter the Range: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if i <=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
"""
#####################################################################
'''
* * * * *  
* * * *    
* * *      
* *        
*   
'''
#--------------------------------------------------------------------
'''
r = int(input("Enter the Range: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if  i+j <= r+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
'''
#####################################################################
'''
*          
  *        
    *      
      *    
        * 
'''
#--------------------------------------------------------------------
'''
r = int(input("Enter the Range: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if i ==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
'''
#####################################################################
"""
        *  
      *    
    *      
  *        
*    
"""
#--------------------------------------------------------------------
"""
r = int(input("Enter the range: ")) + 1
for i in range(1,r):
    for j in range(1,r):
        if i+j == r:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print(" ")
"""
#####################################################################
"""
*       *  
  *   *    
    *      
  *   *    
*       *
"""
#--------------------------------------------------------------------
"""
r = int(input("Enter the Range: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if i ==j or i+j == r+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
"""
#####################################################################
# Some patterns I create by myself, just for curiosity and implementation and fun
'''
*         *         *  
  *       *       *    
    *     *     *      
      *   *   *        
        * * *          
* * * * * * * * * * *  
        * * *          
      *   *   *        
    *     *     *      
  *       *       *    
*         *         * 
'''
#--------------------------------------------------------------------
'''
r = int(input("Enter the range: "))+1
for i in range(1,r):
    for j in range(1,r):
        if i+j == r or i == j or i == r/2 or j == r/2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
'''
#####################################################################
"""
* * * * * * *  
*           *  
*           *  
*           *  
*           *  
*           *  
* * * * * * * 
"""
"""
t = int(input("Enter the range: ")) 
if t%2 == 0:
    print("Please enter an odd number as renge :)")
else:
    for i in range(1,t+1):
        for j in range(1,t+1):
            if i == 1 or j == 1 or i == t or j == t:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print(" ")
"""
# this was my Favourite one :)
'''
* * * * *  
*   *   *  
* * * * *  
*   *   *  
* * * * *  
'''
#t = int(input("Enter the range: ")) 
'''
t = 5
if t%2 == 0:
    print("Please enter an odd number as renge :)")
else:
    for i in range(1,t+1):
        for j in range(1,t+1):
            if i == 1 or j == 1 or i == t or j == t or i == (t+1)/2 or j == (t+1)/2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print(" ")
'''