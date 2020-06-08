# a=1
# def test(a):
#     a= a+1
#     return a

# print(a,"첫번째")
# a=test(a)
# print(a,"두번쨰")

# a=1
# def test():
#     global a 
#     a= a+1

# test()
# print(a)

def add(a,b):
    """add function"""
    return a+b
add.__doc__="add function"
help(add) 