import numpy as np 
a = np.array([1,2,3])
print(a.shape)
print(a.ndim)

dt = np.dtype('i8')
print(dt)

dt2 = np.dtype([('age',np.int8)]) 
print(dt2)

a2=np.array([(10,),(20,)],dtype=dt2)
print(a2)
print(a2.dtype)

#reshape
# 2 X 3 -> 3 X 2
a3 = np.array([[1,2],[3,4],[4,5]])
print(a3, a3.shape, a3.ndim)
a4 =  a3.reshape(2,3)
print(a4, a4.shape, a4.ndim)

#Slicing
a5 = np.array([[1,2],[3,4],[4,5]])
print(a5,a5.shape)
print(a5[0,1],a5[2,0])
print(a5[0],a[2])
print(a5[0][1])


list1 = [1,2,3]
print(list1[:])
a6=np.array([1,2,3,4,5,6,7,8])
print(a6.shape, a6.ndim)
print(a6)
print(type(a6))
print(a6[0:1])
print(type(a6[0:1]))
print(a6[:3])
a7=np.array([[1,2,3],[3,4,5],[6,7,8]])
print(a7.shape,a7.ndim)
print(a7[1:])
