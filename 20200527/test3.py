# # class MyClass:
# #     """아주 간단한 클래스"""
# #     pass
# # print(dir())
# # print(type(MyClass))

# class Person:
#     Name="Default Name"

#     def Print(self):
#         print("My Name is {0}".format(self.Name))

# p1=Person()
# p2=Person()
# #p1.Print()
# print("p1's name:",p1.Name)
# print("p2's name:",p2.Name)

# p1.Name="김연아"
# print("p1's name:",p1.Name)
# print("p2's name:",p2.Name)

# Person.title="New title"
# print("p1's title:",p1.title)
# print("p2's title:",p2.title)
# print("Person's title:",Person.title)

# p1.age=20
# print("p1's age:",p1.age)


# class MyClass:
#     def __init__(self,value):
#         self.value=value
#         print("Class is create! value=",value)

#     def __del__(self):
#         print("Class is deleted!")

# def foo():
#     d=MyClass(10)

# foo()

class CounterManager:
    insCount=0
    def __init__(self):
        CounterManager.insCount+=1
    #def staticPrintInstaceCount(): # 정적메소드 정의
    def staticPrintCount():
        print("Instance Count:",CounterManager.insCount)
    SPrintCount=staticmethod(staticPrintCount) # 정적메서드로 등록 
    
    def classPrintCount(cls): # 클래스 메서드 정의 
        print("Instance Count:",cls.insCount)
    CPrintCount=classmethod(classPrintCount)  #클래스 메소드로 등록


a,b,c = CounterManager(),CounterManager(),CounterManager()
# CounterManager.printInstaceCount()
# b.printInstaceCount()

CounterManager.SPrintCount()  #w정적메서드로 인스턴스 객체 개수를 출력
b.SPrintCount()

CounterManager.CPrintCount() # 클래스 매서드로 인스턴스 객체 개수를 출력 
b.CPrintCount()