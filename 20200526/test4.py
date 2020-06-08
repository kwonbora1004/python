# file = open("file.txt","w")
# for i in range(1,6):
#     data = "안녕하세요.^^"
#     file.write(data)

# print("writed")
# print(file.name)
# file.close()

# file2=open("file.txt","r")
# while True:
#     msg=file2.readline()
#     if not msg : break
#     print(msg)
# file2.close()

# file3 =open("file.txt","r")
# lines=file3.readlines() #리스트반환 
# print(lines)
# for line in lines:
#     print(line)
# file3.close()

# file4=open("file.txt","r")
# lines =file4.read()
# print(lines)
# file4.close()

file5=open("file.txt",'a')
for i in range(2):
    data="Hello java %d \n" %i
    file5.write(data)
file5.close()
print("append")