# def helloFunc():
#     print("Hello Function")

# helloFunc()

# def add(x,y):
#     z=x+y
#     return z

# print(add(1,4))

# a=int(input("a:"))
# b=int(input("b:"))
# print("sum:",add(a,b))

#call by value, reference
#reference
# def test_list(list1):
#     list1.append(20)
#     list1.append(30)
#     print("Inside list:",id(list1),list1)

# list1=[10,30,40,50]

# print(list1)
# test_list(list1)
# print("Outside list:",id(list1),list1)

def add(x,y):
    return x +y
print(add(x=2,y=20))

# print(add(2,y=4))
# print(add(y=2,x=4))

# def subtract(x=0,y=0):
#     return x - y
# print(subtract(x=10))

# def printName(*names):
#     print(type(names))
#     for name in names:
#         print(name)

# printName("이순신","홍길동","권율")
# print(globals())
# printName(1,3,4,5)

def add_andsubtract(a,b):
    return a+b,a-b
    
print(add_andsubtract(2,1))
x,y=add_andsubtract(4,3)
print(x,y)

def msg(str):
    if str =="ok":
        return 
    print("next ok")


msg("good")


data =[(1,2,3),(4,5,6),(6,7,8),(3,2,1)]

for x, y, z in data:
    print(x,y,z)