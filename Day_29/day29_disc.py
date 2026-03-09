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
    intersection1 = set1 & set2
    print(intersection1)
    union1 = set1 | set2
    print(f"The union of Set1 and set2 is union is {union1}")
    print(set1.union(set2))
functions_of_set()    