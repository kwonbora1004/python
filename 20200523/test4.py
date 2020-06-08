dict1={'Name':'홍길동','Age':30}
print(dict1)
print(dict1["Name"])
dict1["Age"]=40
print(dict1)

dict1["hobby"]="복싱"
print(dict1)

del dict1["Age"]
print(dict1)
print(dict1.keys())
print(dict1.values())


for i in dict1:
    print(i)

for i in dict1:
    print(dict1[i])