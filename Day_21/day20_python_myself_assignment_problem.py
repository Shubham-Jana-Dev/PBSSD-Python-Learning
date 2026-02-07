'''
Write a function called average_score that calculates the average of an arbitrary number of scores.
Sample output
average_score(85, 90, 78) -> 84.333...
average_score(100, 95) -> 97.5
average_score() -> 0
'''
def average_score(*args):
    num = 0
    hold = 0
    for i in args:
        num += 1
        hold +=i
    if num == 0 :
        print(0)
    else:
        e = hold/num
        print(e)
average_score(85,90,78)
average_score(100,95)
average_score()
def more_pythonic(*args):
    if not args:
        return 0
    return sum(args)/len(args)
more_pythonic(85,90,78)
more_pythonic(100,95)
more_pythonic()