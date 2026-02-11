def checks(marks):
    if 0 <= marks <= 40:
        return "FAIL"
    elif 40 < marks <= 100:
        return "PASS"
    else:
        return "Invalid Input :("