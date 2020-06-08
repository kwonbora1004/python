# # str="%10s" %"hi"
# # print(str)
# # print(len(str))

# # str2="%-10sjain" %"hi"
# # print(str2)
# # print(len(str2))

# # str3="%.4f" %3.42134234
# # print(str3)
# # print(len(str3))

# # str4 ="%.4f" %3.42134234
# # print(str4)
# # print(len(str4))



# # str5="I am a korean"
# # str6=str5.split()
# # print(str6)
# # print(type(str6))

# list1=['홍길동',100,200]
# print(list1)
# list2=[1,2,3]
# print(list2)
# print(list1[0],list1[1],list1[2])

# str6="%s는 %d원과%d를 가지고 있습니다."%(list1[0],list1[1],list1[2])
# print(str6)

# list3=[0,1,2,3,4,5]
# print(list3[0:])  
# print(list3[:])  
# print(list3[2:4])  
# print(list3[:4])  

# list4=['짜장면','짬뽕','탕수육']
# print(list4)
# list4[0]='팔보채'
# print(list4)

# list5=[1,2,[1,2,3],4,5,[1,2]]
# print(list5)

# print(list5[2])
# del list5[0]
# print(list5)
# list5[0:1]=[10,11,12]
# print(list5)

# colors=['red','green','gold']
# print(colors)
# print(type(colors))

# colors.append('blue')
# print(colors)

# colors.insert(1,'black')
# print(colors)

# colors.extend(['white','gray'])
# print(colors)

# colors+=['red']
# print(colors)

# colors+='red'
# print(colors)

# print(colors.index('red'))

# print(colors.count('red'))

# colors.pop()
# print(colors)
# colors.pop()
# print(colors)

# colors.remove('gold')
# print(colors)
# colors.sort()
# print(colors)
# colors.reverse()
# print(colors)

# list6=[1,[1,2,3],4,[1,2,[1,2,3]]]
# print(list6)
# print(list6[1][2])
# print(list6[3][2][2])
# print(list6[:2])
# print(list6[-4:3])

# str="%0.4f" %3.4533421
# print(str)
# print(str.split(".")[1])

# def add(a,b):
#     return a+b

# print(add(1,4))

# list7=[1,2,3,4,5,6,]
# for i in list7:
#     print(i)

# tu1 =(100,"홍길동",200)
# print(tu1)
# print(tu1[0])
#del tu1[0]
#tu1[0]=10
tu2=(1,2,3,4,5)
print(tu2[0],tu2[0:2])

#[]리스트 () 튜플  {}사전
tu3=[(10,"영업부",100),(20,"회계부",300)]
print(tu3)

tu4=(1,(10,20),(30,40,50))
print(tu4)

for i in tu3:
    print(i)