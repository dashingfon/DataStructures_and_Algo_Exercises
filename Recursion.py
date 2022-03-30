'''
Using reccursion to sum a list of numbers
'''

num = [
    3,
    4,
    3,
    6,
    12,
    4,
    16,
    12
]

def addNums(lst):
    if len(lst) > 0:
        return lst.pop(0) + addNums(lst)
    else:
        return 0


print(addNums(num))


