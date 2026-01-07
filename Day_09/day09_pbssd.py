# Check a digit vs character recognition
'''
e = input("Enter a char....")
if('0'<=e<='9'):
    print("It's a digit")
else:
    print("It's a charecter")
'''
# positive/negative even/odd analysis
x = int(input("Enter number:-"))
if(x>=0):
    if(x%2 == 0):
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    if(x%2 == 0):
        print("Nagetive and even")
    else:
        print("Nagetive and odd")