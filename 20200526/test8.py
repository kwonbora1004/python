# print(1)
# print('h1,guyz')
# a='hello\n'
# print(a)

# x=0.2
# print(x)
# str(x)
# print(str(x))
# a=repr('hello\n')
# print(a)

# print(x,'test')
# print(a+'this is test')

# import sys
# print("welcome to","python",sep="~",end="!",file=sys.stderr)
# f=open('test.txt','w')
# print("file write",file=f)
# f.close()

# for x in range(1,6):
#     print(x,"*",x,"=",x*x)

# for x in range(1,6):
#     print(x,"*",x,"=",str(x*x).center(5))


# for x in range(1,6):
#     print(x,"*",x,"=",str(x*x).zfill(5))

# print("{0} is {1}".format("apple","red"))
# print("{0} is {1} or {2}".format("apple","red","green"))

# a=input('insert any keys:')
# print(a)

f=open('test.txt')
f.read()
f.tell() #어디까지 읽었나 확인
f.seek()# 처음으로 
f.read()# 처음부터 다시읽게됨 
f.seek()
f.readline() # 처음부터 줄단위로 
f.readlines() #줄단위로 모두 리스트로 