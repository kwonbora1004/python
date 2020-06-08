# class A:
#     def __init__(self, a):
#         self.a = a
#     def __add__(self, o):
#         return self.a * o.a

# a = A(4)
# b = A(2)
# c = a.__add__(b)
# c2 = a + b
# print(c, c2)

# (1,2) + (3, 4) -> (4, 6)
# t = Test(1,2)
# t2 = Test(3,4)
# t + t2
# (4, 6)
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, v):
        return self.a + v.a, self.b + v.b

t = Test(1,2)
t2 = Test(3,4)
t3 = t + t2
t4 = t.__add__(t2)
print(t3)


