print('~期末考結束了，校長要發獎學金~')
print('校長:各位同學大家好，我是校長。把你的數學成績及英語成績輸入，若兩科都及格，我會給你獎學金!')
score1 = int(input('先從你開始。你的數學成績是?'))
score2 = int(input('那你的英文成績呢?'))
print(score1)
if score1>60:
    print('真棒!')
    print(score2)
    if score2>60:
       input('非常棒!你的名字是?')
    else:print('請你去罰站。')
else:print('請你去罰站。')