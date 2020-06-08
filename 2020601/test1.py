# print("my module")

# if __name__ =='__main__':
#     print("모듈을 직접실행하셧네요")
# else:
#     print("임포트 하셧네요.")
 

# #모듈명:myfunc
# #함수 myhome

# def myhome():
#     print("오늘은 비가옵니다.")

# print(__name__)
# if __name__=="__main__":
#     myhome()
# def add(x,y):
#     return x +y

# def mulply(x,y):
#     return x * y 

# def divide(x,y):
#     return x/y

# def subtrace(x,y):
#     return x-y
# print(__name__)

# if __name__=='__main__':   # 메인할떄만 수행  모듈 일때는X
#     print(add(2,1))
#     print(mulply(2,2))
# def add(a,b):
#     return a+b

# def subtract(a,b):
#     return a-b
# # print(1)
# # print('h1,guyz')
# # a='hello\n'
# # print(a)

# # x=0.2
# # print(x)
# # str(x)
# # print(str(x))
# # a=repr('hello\n')
# # print(a)

# # print(x,'test')
# # print(a+'this is test')

# # import sys
# # print("welcome to","python",sep="~",end="!",file=sys.stderr)
# # f=open('test.txt','w')
# # print("file write",file=f)
# # f.close()

# # for x in range(1,6):
# #     print(x,"*",x,"=",x*x)

# # for x in range(1,6):
# #     print(x,"*",x,"=",str(x*x).center(5))


# # for x in range(1,6):
# #     print(x,"*",x,"=",str(x*x).zfill(5))

# print("{0} is {1}".format("apple","red"))
# print("{0} is {1} or {2}".format("apple","red","green"))

# a=input('insert any keys:')
# print(a)

# python

 

# import calcuation as cal
# r=cal.add(2,5)
# r2=cal.divide(4,2)
# r3=cal.mulply(5,4)
# r4=cal.subtrace(2,1)

# print(r,r2,r3,r4)

# print(dir(cal))
# import sys
# paths=sys.path
# print(paths)
# sys.path.append("c:\\Python_modules")

# import calc2 
# c=calc2.add(4,5)
# print(c)
# # import calc
# # c=calc.add(1,2)
# # print(c)

# # c2=calc.subtract(5,4)
# # print(c2)

# # from calc import add
# # c3=add(2,4)
# # print(c3)

# #import 모듈
# # form 모듈 import 모듈함수 

# # form calc import add,subtract
# # c4=add(3,5)
# # c5=subtract(5,2)

# from calc import *
# c6=add(5,6)
# c7=subtract(8,8)
# print(c6,c7)

# #pythonpath
# # file = open("file.txt","w")
# # for i in range(1,6):
# #     data = "안녕하세요.^^"
# #     file.write(data)

# # print("writed")
# # print(file.name)
# # file.close()

# # file2=open("file.txt","r")
# # while True:
# #     msg=file2.readline()
# #     if not msg : break
# #     print(msg)
# # file2.close()

# # file3 =open("file.txt","r")
# # lines=file3.readlines() #리스트반환 
# # print(lines)
# # for line in lines:
# #     print(line)
# # file3.close()

# # file4=open("file.txt","r")
# # lines =file4.read()
# # print(lines)
# # file4.close()

# file5=open("file.txt",'a')
# for i in range(2):
#     data="Hello java %d \n" %i
#     file5.write(data)
# file5.close()
# print("append")
 

# # a=1
# # def test(a):
# #     a= a+1
# #     return a

# # print(a,"첫번째")
# # a=test(a)
# # print(a,"두번쨰")

# # a=1
# # def test():
# #     global a 
# #     a= a+1

# # test()
# # print(a)

# def add(a,b):
#     """add function"""
#     return a+b
# add.__doc__="add function"
# help(add) 

# import company.myfunc1
# myhome1()

# company.myfunc1.myhome1()

# from company.myfunc1 import myhome1

# # def test(a):
# #     return a +10

# # print(test(2))

# # b=test
# # print(id(b),type(b),id(test),type(test))
# # print(b(3))

# # f=lambda a: a+10
# # print(f(2))
# # f2=lambda a,b: a+b
# # print(f2(3,2))

# # def t(n):
# #     return lambda a:a*n

# # n = int(input("단수를 입력해주세요:"))
# # b=t(n)
# # print(type(b))
# # for i in range(1,10):
# #     print(n,"x",i,"=",b(i))

# # def gugudan(a):
# #     return a *21

# list1 = {1,2,3,4,10,123,22}
# print(type(list1))
# odd = list(filter(lambda x: (x%3==0),list1))
# print(odd)

# list2 =list(map(lambda x: x*x,list1))
# print(list2)

# # str = "python is happy"
# # for word in str:
# #     print(word)

# # list=['red','blue','yello']
# # for color in list:
# #     print(color)

# # tuple=('red','blue','yello')
# # for color in tuple:
# #     print(color)

# # for inx in range(1,10):
# #     print(inx)

# # for index in range(len(list)):
# #     print(list[index])

# # data = [(1,2),(3,4),(4,5)]
# # for x, y in data:
# #     print(x,y)

# # l='Hello'
# # d=[s for s in l]
# # print(d)

# # d2=[(x*2,y*4)for (x,y)in data]
# # print(d2)

# # def add(a,b,c=0):
# #     return a+b+c

# # c= add(1,2)
# # print(c)

# # c2 = add(1,2,3)
# # print(c2)

# def msgPrint(str):
#     print(str)

# #call by reference
# def changeList(list2):
#     list3=[4,5,6,7]
#     list2.append(list3)
#     print(id(list2),list2)

# list1=[1,2,3]
# changeList(list1)
# print(id(list1),list1)

# def printName(name,*msg):
#     print(name)
#     print(msg)

# printName('강감찬',1,2)

# from 모듈 import함수
# from 패키지 import모듈

 

# print("my module")

# if __name__ =='__main__':
#     print("모듈을 직접실행하셧네요")
# else:
#     print("임포트 하셧네요.")
 

# #모듈명:myfunc
# #함수 myhome

# def myhome():
#     print("오늘은 비가옵니다.")

# print(__name__)
# if __name__=="__main__":
#     myhome()
# def add(x,y):
#     return x +y

# def mulply(x,y):
#     return x * y 

# def divide(x,y):
#     return x/y

# def subtrace(x,y):
#     return x-y
# print(__name__)
# if __name__=='__main__':   # 메인할떄만 수행  모듈 일때는X
#     print(add(2,1))
#     print(mulply(2,2))
# def add(a,b):
#     return a+b

# def subtract(a,b):
#     return a-b
# # print(1)
# # print('h1,guyz')
# # a='hello\n'
# # print(a)

# # x=0.2
# # print(x)
# # str(x)
# # print(str(x))
# # a=repr('hello\n')
# # print(a)

# # print(x,'test')
# # print(a+'this is test')

# # import sys
# # print("welcome to","python",sep="~",end="!",file=sys.stderr)
# # f=open('test.txt','w')
# # print("file write",file=f)
# # f.close()

# # for x in range(1,6):
# #     print(x,"*",x,"=",x*x)

# # for x in range(1,6):
# #     print(x,"*",x,"=",str(x*x).center(5))


# # for x in range(1,6):
# #     print(x,"*",x,"=",str(x*x).zfill(5))

# print("{0} is {1}".format("apple","red"))
# print("{0} is {1} or {2}".format("apple","red","green"))

# a=input('insert any keys:')
# print(a)

# python

 

# import calcuation as cal
# r=cal.add(2,5)
# r2=cal.divide(4,2)
# r3=cal.mulply(5,4)
# r4=cal.subtrace(2,1)

# print(r,r2,r3,r4)

# print(dir(cal))
# import sys
# paths=sys.path
# print(paths)
# sys.path.append("c:\\Python_modules")

# import calc2 
# c=calc2.add(4,5)
# print(c)
# # import calc
# # c=calc.add(1,2)
# # print(c)

# # c2=calc.subtract(5,4)
# # print(c2)

# # from calc import add
# # c3=add(2,4)
# # print(c3)

# #import 모듈
# # form 모듈 import 모듈함수 

# # form calc import add,subtract
# # c4=add(3,5)
# # c5=subtract(5,2)

# from calc import *
# c6=add(5,6)
# c7=subtract(8,8)
# print(c6,c7)

# #pythonpath
# # file = open("file.txt","w")
# # for i in range(1,6):
# #     data = "안녕하세요.^^"
# #     file.write(data)

# # print("writed")
# # print(file.name)
# # file.close()

# # file2=open("file.txt","r")
# # while True:
# #     msg=file2.readline()
# #     if not msg : break
# #     print(msg)
# # file2.close()

# # file3 =open("file.txt","r")
# # lines=file3.readlines() #리스트반환 
# # print(lines)
# # for line in lines:
# #     print(line)
# # file3.close()

# # file4=open("file.txt","r")
# # lines =file4.read()
# # print(lines)
# # file4.close()

# file5=open("file.txt",'a')
# for i in range(2):
#     data="Hello java %d \n" %i
#     file5.write(data)
# file5.close()
# print("append")
 

# # a=1
# # def test(a):
# #     a= a+1
# #     return a

# # print(a,"첫번째")
# # a=test(a)
# # print(a,"두번쨰")

# # a=1
# # def test():
# #     global a 
# #     a= a+1

# # test()
# # print(a)

# def add(a,b):
#     """add function"""
#     return a+b
# add.__doc__="add function"
# help(add) 

# import company.myfunc1
# myhome1()

# company.myfunc1.myhome1()

# from company.myfunc1 import myhome1

# # def test(a):
# #     return a +10

# # print(test(2))

# # b=test
# # print(id(b),type(b),id(test),type(test))
# # print(b(3))

# # f=lambda a: a+10
# # print(f(2))
# # f2=lambda a,b: a+b
# # print(f2(3,2))

# # def t(n):
# #     return lambda a:a*n

# # n = int(input("단수를 입력해주세요:"))
# # b=t(n)
# # print(type(b))
# # for i in range(1,10):
# #     print(n,"x",i,"=",b(i))

# # def gugudan(a):
# #     return a *21

# list1 = {1,2,3,4,10,123,22}
# print(type(list1))
# odd = list(filter(lambda x: (x%3==0),list1))
# print(odd)

# list2 =list(map(lambda x: x*x,list1))
# print(list2)

# # str = "python is happy"
# # for word in str:
# #     print(word)

# # list=['red','blue','yello']
# # for color in list:
# #     print(color)

# # tuple=('red','blue','yello')
# # for color in tuple:
# #     print(color)

# # for inx in range(1,10):
# #     print(inx)

# # for index in range(len(list)):
# #     print(list[index])

# # data = [(1,2),(3,4),(4,5)]
# # for x, y in data:
# #     print(x,y)

# # l='Hello'
# # d=[s for s in l]
# # print(d)

# # d2=[(x*2,y*4)for (x,y)in data]
# # print(d2)

# # def add(a,b,c=0):
# #     return a+b+c

# # c= add(1,2)
# # print(c)

# # c2 = add(1,2,3)
# # print(c2)

# def msgPrint(str):
#     print(str)

# #call by reference
# def changeList(list2):
#     list3=[4,5,6,7]
#     list2.append(list3)
#     print(id(list2),list2)

# list1=[1,2,3]
# changeList(list1)
# print(id(list1),list1)

# def printName(name,*msg):
#     print(name)
#     print(msg)

# printName('강감찬',1,2)

