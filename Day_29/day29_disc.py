def disc_s():
    My_info = {'name':'Shubham','age':19,'role':'Student','current year':2025}
    My_info['current year'] = 2026
    print(My_info)

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
find_success()