print("###################계산기###################")
print("############################################")
print("#1.덧셈\n#2.뺄셈\n#3.나눗셈\n#4.곱셈\n#5.종료")
print("############################################")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

def msg():
    
    a=int(input("첫번째 숫자를 입력해주세요"))
    cal=(input("연산자를 입력해주세요"))
    b=int(input("두번째 숫자를 입력해주세요 "))
    return a , b
while True:

    num = int(input("#원하는 메뉴를 입력해주세요.[1-5]"))
    if num==1:
        msg()
        # if cal !="+":
        #     print("연산자를 +로 입력하세요")
        #     break
        print("결과는", add(a,b),"입니다")

    elif num ==2:
        a=int(input("첫번째 숫자를 입력해주세요"))
        cal=(input("연산자를 입력해주세요"))
        b=int(input("두번째 숫자를 입력해주세요 "))
        print("결과는", sub(a,b),"입니다")


    elif num==3:
        a=int(input("첫번째 숫자를 입력해주세요"))
        cal=(input("연산자를 입력해주세요"))
        b=int(input("두번째 숫자를 입력해주세요 "))
        print("결과는", div(a,b),"입니다")

    elif num==4:
        a=int(input("첫번째 숫자를 입력해주세요"))
        cal=(input("연산자를 입력해주세요"))
        b=int(input("두번째 숫자를 입력해주세요 "))
        print("결과는", mul(a,b),"입니다")
    else:
        print("종료합니다.")
        break


