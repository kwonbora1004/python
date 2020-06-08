colors=['blue','green','red','white']
print(colors)
colors.sort()
print(colors)
print(sorted(['blue','green','red','white']))

def mysort(x):
    return x[-1]

print(mysort('white'),mysort('red'))


colors2=['blue','green','red','white']
colors2.sort(key=mysort)
print(mysort("white"),mysort('red'),mysort('green'),mysort('blue'))

#얕은복사, 깊은복사 
a1=1
b1=a1
print(a1,b1)
list1=[1,2,3]
list2=list1

print(list1,list2)

print(id(list1),id(list2))
print(id(a1),id(b1))

#shallow copyy
s=list1[:]
print(list1,s)
s.append([5,5])
print(list1,5)

