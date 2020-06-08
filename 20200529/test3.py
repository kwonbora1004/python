# import numpy as np 
# a=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# print(a.ndim, a.shape)
# print(a[0,0],a[3,2])
# print(a[:,:])
# print(a[[0,2],1:])
# print(a[-1])
# print(a[-1:,-1:])

# print(a[a>10])
# print(a[a>=5])

# #dtype
# a2=np.arange(24)
# print(a2)
# print(a2.ndim)

# b2=a2.reshape(2,4,3)
# print(b2)

# a3=np.empty([3,2],dtype=int)
# print(a3)

# a4=np.zeros(5)
# print(a4,a4.dtype)
# a5=a4.astype(int)
# print(a5.dtype)
# print(a5)

# import numpy as np 
# a6 = np.empty([3,2],dtype=int)
# print(a6)

# a7=np.zeros((5,),dtype=np.int)
# print(a7)
import numpy as np 
# x =  [1, 2, 3, ]
# a = np.asarray(x)
# print(a.shape, a.ndim)

x1 = np.arange(5)
print(x1)
x2 =  list(range(5))
print(x2) 

x3 = np.arange(10,20,2)
print(x3)

a1 = np.array([1, 2, 3, 4 ])
b2 = np.array([10, 20, 30, 40])
c2 = a1 * b2
print(c2)

a3 = np.array([[0,0,0],\
              [10,10,10],\
              [20,20,20],\
              [30,30,30]])

a4 = np.array([0,1,2])
a5 = a3 + a4
print(a5)

            