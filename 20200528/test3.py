# try:
#     a=int(input("a:"))
#     b=int(input("b:"))

#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("error")
# else:
#     print("ok")


# def divide(a,b):
#     return a/b
  
# try:
#    c=divide(5,2)
# except ZeroDivisionError:
#     print("두번째 인자는 0이어서는 안됩니다.")
# except TypeError:
#     print("모든인자는 숫자여야합니다.")
# except:
#     print("ZeroDivisionError,TypeError를 제외한 다른에러")
# else:
#     print("Result:{0},",format(c))
# finally:
#     print("항상 finally블록은 수행됩니다.")

class NedaticeDicisionError(Exception):
    def __init__(self,value):
        self.value=value

def PositiveDivide(a,b):
    if(b<0):
        raise NedaticeDicisionError(b)
    return a/b

try:
    ret=PositiveDivide(10,-3)
    print('10/3={0}'.format(ret))
except NedaticeDicisionError as e:
    print('Error-Second argument of PositiveDicide is',values)
except ZeroDivisionError as e:
    print('Error-',e.args[0])
except:
    print("Unexpected exception!")