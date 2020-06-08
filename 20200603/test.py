#비만도 계산법 bmi 지수 =몸무게(kg) /(  신장(m)   X   (신장(m)   )) 신장 cm 
import numpy as np 
import pandas as pd 

data = pd.read_csv("C:\\Python37_Project\\20200603\\student.csv")
#print(data['weight']/ data['height'])
filter = data['sex'] == 'male'
#print(data[filter])
df_male = data [filter]


filter2 = data['sex'] == 'female'
#print(data[filter2])
df_female = data [filter2]
#print(df_male)
#print(df_female)


df_male['bmi'] = df_male['weight'] *10000 / (df_male['height'] * df_male['height'])

df_female['bmi'] = df_female['weight'] *10000 / (df_female['height'] * df_female['height'])

#print(df_female['bmi'].mean())
#print(df_male['bmi'].mean())


while(True):
    print("#########################남녀 평균BMI 지수#########################")
    choice = input("알고 싶은 평균 BMI지수의 성별을 입력해주세요. 남자(1) 여자(2) : ")
    if choice == "1" :
        print(df_male['bmi'].mean())
    elif choice == "2" :
        print(df_female['bmi'].mean())
    else :
        break

