def disc_s():
    My_info = {'name':'Shubham','age':19,'role':'Student','current year':2025}
    My_info['current year'] = 2026
    print(My_info)
# disc_s()

def the_challange():
    attendance_log = {"Jannuary":100,"February":100,"March":100}
    attendance_log["April"] = 100
    print(attendance_log["February"])
# the_challange()

def the_future():
    t_f = {"Year":2036,"Age":29,"Role":"senior developer"}
    print(t_f.keys())
# the_future()

def find_success():
    f_s = {"Year":2036,"Age":29,"Role":"senior developer"}
    f_s["Status"] = "Success"
    if "Status" in f_s:
        print("I have achieved it.")
    else:
        print("Still under process.")
# find_success()

def student_status():
    student_info = {"Ram":{'status':'Pass'},"Bikash":{'status':'fail'},"Neha":{'status':'Pass'},"Rahul":{'status':'fail'},"Sukamal":{'status':'Pass'}}
    count = 0
    for i in student_info:
        if student_info[i].get("status") == "Pass":  #.get('status')
            print(i)
            count += 1
    print(f"The total number of passed students: {count}")
# student_status()

def future():
    lmg_2036 = {"Arjuna":2, "Mimi":3, "Neha":5, "Shanvi":1, "Pooja":4}
    if "Shanvi"  in lmg_2036:
        print(lmg_2036["Shanvi"])
    else:
        print("Shanvi is not in the list, wait for 2036.")
    # update Mimi's roll number.
    lmg_2036['Mimi'] = 10
    print(list(lmg_2036)) # roll numbers are not printing. :(
    roll = []
    for i in lmg_2036:
        roll.append(f"name = {i} roll = {lmg_2036[i]}")
    print(roll) # now roll numbers are also printing :)
    lmg_2036.pop("Pooja")
    print(lmg_2036)
#future()

def functions_of_set():
    set1 = {1,2,3,4,5,6,"Shubham","Raj","Doremon","Hello",34,45}
    set2 = {'Shubham',4,5,6,'Hello',10,11,12,13,14,15,16,'seven'}
    union1 = set1 | set2 # returns all elments of both set
    print(f"The union of Set1 and set2 (by using '|' symbol) is {union1}")
    print(f"The union of set1 and set2 (by .union keyword) is {set1.union(set2)}")
    intersection1 = set1 & set2 # returns only the common elements 
    print(f"The intersection of set1 and set2 (by using '&' symbol) {intersection1}")
    print(f"The intersection of set1 and set3 (by .intersection keyword) is {set1.intersection(set2)}")
    difference1 = set1 - set2 # returns the elements present in the set1 but in the set2
    print(f"set1 - set2 = {difference1}")
    print(f"set2 - set1 = {set2.difference(set1)}") 
    symmetric_difference1 = set1 ^ set2  # returns all the elements exsept the common elements
    print(f"set2 ^ set1 = {set2.symmetric_difference(set1)}")
    print(f"set1 ^ set2 = {symmetric_difference1}")
    setA = {1,2,3,4,"Hi",5,6,7,8,9}
    setB = {1,4,5,"Hi",6,9}
    setC = {122,433,"Shubham"}
    print(setA.issubset(setB))
    print(setB.issubset(setA))
    print(setA.issuperset(setB))
    print(setB.issuperset(setA))
    print(setA.isdisjoint(setC)) # True if two sets have no elements in common
    setC.add(354)
    setC.update([443,90])
    setC.remove(443)
    setC.discard(90)
    setC.discard('h') # will run
    print(setC)
    setC.clear() # to delete all elements from a list
    #setC.remove('h') will not run
# functions_of_set()    

def function_of_tuple():
    my_tuple = (4,5,6,3,7,4,"Shubham","Python","Branch",4,3,90,100)
    print(my_tuple.count(5))
    print(4 in my_tuple)
    print(my_tuple.count("Shubham"))
    my_tuple = (23,34,12,33,55,67,89,32,21,15)
    print(sorted(my_tuple))
    tuple_a = (1,5,3,2,6,4,3,7,9,8,23,13)
    print(tuple(sorted(tuple_a,reverse = True)))
function_of_tuple()

def challenges():
    db1 = {"id1":"Shubham","id2":"Raj"}
    db2 = {"id2":"Raj","id3":"Sulekha"}
    db3 = {key: db1[key] for key in db1 if key in db2}
    db4 = db1 | db2
    print(db3)
    print(db4)
challenges()

    
