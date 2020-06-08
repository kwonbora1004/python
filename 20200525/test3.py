# a=int(input("첫번째 숫자"))
# b=int(input("두번째 숫자"))
# c=int(input("세번째 숫자"))

# if a > b and a > c:
#     print("a는 가장크다")
# if b > a and b > c:
#     print("b는 가장크다")
# if c > a and c > b:
#     print("C는가장크다")

# age=int(input("당신의 나이를 입력해주세요"))
# if age >=18:
#     print("당신은 성인입니다.")
# else:
#     print("당신은 미성년입니다.")

# name = input("당신의 이름을 입력해주세요:")
# if name=="홍길동":
#     print("당신은 홍길동이군요")
# elif name=="이순신":
#     print("당신은 이순신 입니다.")
# elif name=="강감찬":
#     print("당신은 강감찬입니다.")
# else:
#     print("누구세요")

# pocket=['paper','cellphone']
# card =1
# if 'money'in pocket:
#     print("택시타세요")
# elif card:
#     print("택시타세요")
# else:
#     print("걸어가세요")

# a =1 
# if a ==1:
#     pass
# else:
#     print("??")

# i=1
# while i<=10:
#     print(i)
#     i=i+1

# inx = int(input("숫자입력"))
# while inx <= 100:
#     print(inx)
#     inx =inx +1

#숫자를 입력받아 해당하는 구구단을 출력하시오

# inx = int(input("숫자입력"))
# jnx= 1
# while jnx <=9:
#     print("%d X %d =%d\n" %(inx,jnx,inx*jnx))
#     # print(inx* jnx)
#     jnx += 1

# import time
# while True:
#     n = int(input("Chocice the number"))
#     if n ==0:
#         print("sleep 3 second form now on...")
#         time.sleep(3)
#         print("Terminated")
#         break

# i = 1 
# n = int(input("숫자입력하세용"))
# for i in range(0,11):
#     print("%d X %d = %d" % (n,i,n*i))

# l=[1,2,3,4]
# for j in l:
#     print(j)


# test =[(1,2),(3,4),(5,6)]
# for (a,b) in test:
#     print(a,b)

# marks =[90,25,67,45,80]
# number =0
# for mark in marks:
#     number = number+1
#     if mark >=60:
#         print("%d 번학생은 합격입니다."%number)
#     else:
#        print("%d 번학생은 불합격입니다."%number)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j, end =" ")
#     print('')


# print(list(range(10)))
# print(list(range(2,10)))



# while True:
#     print("1.덧셈\n2.뺄셈\n3.나눗셈\n4.곱셈")
#     num = int(input("메뉴를 입력해주세요[1-4]"))
#     if num==1:
#         print("덧셈입니다")
#         a=int(input("첫번째 숫자를 입력해주세요"))
#         b=int(input("두번째 숫자를 입력해주세요 "))
#         print("결과는 %d 입니다."%(a+b))
#     elif num ==2:
#         print("뺄셈입니다.")
#         a=int(input("첫번째 숫자를 입력해주세요"))
#         b=int(input("두번째 숫자를 입력해주세요 "))
#         print("결과는 %d 입니다."%(a-b))
#     elif num==3:
#         print("나눗셈입니다.")
#         a=int(input("첫번째 숫자를 입력해주세요"))
#         b=int(input("두번째 숫자를 입력해주세요 "))
#         print("결과는 %d 입니다."%(a/b))
#     elif num==4:
#         print("곱셈입니다.")
#         a=int(input("첫번째 숫자를 입력해주세요"))
#         b=int(input("두번째 숫자를 입력해주세요 "))
#         print("결과는 %d 입니다."%(a*b))
#     else:
#         print("종료합니다.")
#         break

# letters=[]
# for letter in 'Python':
#     letters.append(letter)

# print(letter)

# str= [letter for letter in 'python']
# print(str)

# a=[1,2,3,4]
# r=[]
# for n in a : 
#     r.append(n)
# print(r)
# #a1=[n for n in  a]
# a1=[n for n in  a if n %2 ==0]
# print (a1)

# L=[10,12,14,16,18]
# for i in L:
#     print(i)


# list(range(10))
# for i in range(10,20,2):
#     print(i)

# L=[100,15.5,"apple"]
# for i in enumerate(L):
#     print(i)

l=[1,2,3,4,5]
[i **2 for i in 1]

t=("apple","banana","orange")
[len(i) for i in t]

d={100:"apple",200:"banana",300:"orange"}
[v.upper() for v in d.values()]
[i** 3 for i in range(5)]