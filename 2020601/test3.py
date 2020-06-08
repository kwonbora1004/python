import numpy as np 

x = np.random.randint(100,size=10)
print(x)

print(x[3])

print(x[3],x[7],x[2])
print(x[[3,7,2]])

index = [3,7,2]
print(x[index])

x2 = np.arange(12).reshape((3,4))
print(x2)

row = np.array([0,1,2])
col = np.array([2,1,3])
print(x2[row,col])

x3 = np.random.rand(6)
print(x3)

x4 = np.random.rand(3,2)
print(x4)
print('')
#153,156
arr = np.empty((8,4))
for i in range(8):
    arr[i] = i
    print(arr)
    print('')
    print(arr[[4,3,0,6]])
    print(arr[[-3,-5,-7]])

arr = np.arange(32).reshape((8,4))
print(arr)
print(arr[[1,5,7,2],[0,3,1,2]])

arr = np.arange(15).reshape((3,5))
print(arr)
print(arr.T)


arr = np.random.randn(6,3)
print(arr)
print(np.dot(arr.T,arr))