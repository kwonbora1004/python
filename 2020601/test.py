import numpy as np 
a = np.array([1,2,3,4])
print(a,a.shape,a.ndim)

l=[[1,2],[3,4]]
print(l[0][0])

a1= np.array([[1,2],[3,4]])
print(a1,a1.shape,a.ndim)

l2=[[[1,2],[2,3]]]
a2=np.array(l2)
print(a2,a2.shape,a2.ndim)
print(l2[0][0][1])


a3=np.array([1,2,3,4],ndmin=2)
print(a3.shape,a3.ndim,a3.dtype)

a4=np.array([1,2,3,4],dtype=float)
print(a4,a4.shape,a4.ndim,a4.dtype)

Student = np.dtype([('name','S20'),('age','i1')])
print(Student)

a5=np.array([('test',20),('test2',30)],dtype=Student)
print(a5,a5.shape,a5.ndim)

a6=np.empty([4,3],dtype=int)
print(a6)

a7=np.zeros((10,),dtype=np.int)  # int  np.int 동일
print(a7)

a8=np.ones([2,2],dtype=int)    #2,2사이즈
print(a8)

a9 = np.arange(10,dtype=float)
print(a9)

a10 = np.arange(10,20,2) #2씩증가 
print(a10)

a11 = np.linspace(10,20,5) #구간을 5로나눔
print(a11)

a12 = np.linspace(1,2,5)
print(a12)

a13 = np.arange(10)
print(a13)

a14 = slice(2,7,2)
print(a13[a14])

print(a13[2:7:2])

a15 = np.arange(10)
print(a15)
#[0 1 2 3 4 5 6 7 8 9]
print(a15[2:4])

a16 = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a16[1:])

x = np.array([[1,2],[3,4],[5,6]])
y = x[[0,1,2],[0,1,0]]
print(x) 
print(y)

y2 = x[1:2,[0,1,0]]
print(y2)

y3 = x[x>2]
print(y3)

r = range(5)
lt = list(r)
print(iter(lt))

for i in iter(lt): #데이터 뽑아내기 .. 
    print(i)
print('')

a17 = np.array([1,2,3,4])
for i in a17:
    print(i)
print('')

for i2 in np.nditer(a17):  #위와 동일
    print(i2)

list3 = [[1,2],[3,4]]
for i2 in list3:
    print(i2)

a18 = np.array(list3)
for i2 in a18:
    print(i2) 

print(a18.shape)
for i2 in np.nditer(a18):
    print(i2)

list4 = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
a19 = np.array(list4)
for i2 in a19:
    print(i2)

for i2 in np.nditer(a19):  #하나씩 출력
    print(i2)

arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d[0])

old_values = arr3d[0].copy()
arr3d[0]=42
print(arr3d)

arr3d[0]=old_values
print(arr3d)

print(arr3d[1,0])
x = arr3d[1]
print(x)

print(x[0])