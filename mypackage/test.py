from mymod import *
import numpy as np

print("*덧셈")
a = int(input("첫번째숫자를 입력해주세요:"))
b = int(input("두번째숫자를 입력해주세요:"))
print(a,"+",b,"의 결과는", add(a,b),"입니다")



print("*곱셈")
a = int(input("첫번째숫자를 입력해주세요:"))
b = int(input("두번째숫자를 입력해주세요:"))
print(a,"*",b,"의 결과는",multiply(a,b),"입니다")

print("*뺄셈")
a = int(input("첫번째숫자를 입력해주세요:"))
b = int(input("두번째숫자를 입력해주세요:"))
print(a,"-",b,"의 결과는",subtract(a,b),"입니다")

print("*나눗셈")
a = int(input("첫번째숫자를 입력해주세요:"))
b = int(input("두번째숫자를 입력해주세요:"))
print(a,"/",b,"의 결과는", divide(a,b),"입니다")



data = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
data = np.array(data)
print(data)

num=data[data%2==0]
print("짝수의 합은",num.sum())
