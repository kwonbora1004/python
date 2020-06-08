class Employee5:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee5.empCount+=1
    def displayCount(self):
        print("Employee %d "%Employee5.empCount)

    def displayEmployee(self):
        print("name:",self.name,"salary:",self.salary)

emp1=Employee5("홍길동",3000)
emp1.displayCount()
emp1.displayEmployee()

emp2=Employee5("이순신",3300)
emp2.displayCount()
emp2.displayEmployee()
print(emp2.__dict__)
print(Employee5.__dict__)


class Animal:
    def breath(self):
        print("Animal breathing")
    def eat(self, name="강아지",age=20):
        self.name=name
        self.age=age

class Dog(Animal):
    def bark(self):
        print("Dog barking")
    def breath(self): ##overriding
        print("Dog breathing")

d=Dog()
d.bark()
d.breath()

a=Animal()
a.eat(name="강아지2")
a.eat("강아지3",50)

class MyData:   ##__private delare
    __c=10
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.__c=c # datahide 
    def displayData(self):
        print(self.a, self.b)
    def __displayData2(self):
        print("nothing")
    def __del__(self):
        print("Delete")

myData=MyData(1,2,3)
print(myData.a)
#print(myData.__c)
#myData.__displayData2()
myData.__del__()

class Calc1:
    def Add(self,a,b):
        return a+b
class Calc2:
    def multiply(self,a,b):
        return a*b

class Calc3(Calc1,Calc2):
    def divide(self,a,b):
        return a/b

c=Calc3()
print(c.Add(1,2))
print(c.multiply(3,2))
print(c.divide(4,2))

