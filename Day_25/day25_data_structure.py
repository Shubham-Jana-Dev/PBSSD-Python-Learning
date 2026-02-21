x = [[[['A',['B','C']],'D'],['E','F']],[['I',['G','H']],['J',['K','L']]]]
print("-------List Printing-------")
print(x) # whole list
print(x[0])
print(x[1])
print(x[0][0])
print(x[0][1])
print(x[0][0][0])
print(x[0][0][0][1])
print(x[1][0])
print(x[1][1])
print(x[1][0][1])
print(x[1][1][1])
print("-------Individual Element Printing-------")
print(x[0][0][0][0]) # A
print(x[0][0][0][1][0]) # B
print(x[0][0][0][1][1]) # C
print(x[0][0][1]) # D
print(x[0][1][0]) # E
print(x[0][1][1]) # F
print(x[1][0][0]) # I
print(x[1][0][1][0]) # G
print(x[1][0][1][1]) # H
print(x[1][1][0]) # J
print(x[1][1][1][0]) # K
print(x[1][1][1][1]) # L