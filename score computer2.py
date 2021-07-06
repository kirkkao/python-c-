score = input('您的成績?')
score2 = float(score)
print(score)
print(type(score))
print(type(score2))
if score2>100:
    print('A+')
elif score2<100 and score2>80:
    print('A')
elif score2<80 and score2>60:
    print('B')
elif score2<60 and score2>40:
    print('C')
elif score2<40 and score2>20:
    print('D')
elif score2<20 and score2>0:
    print('E')