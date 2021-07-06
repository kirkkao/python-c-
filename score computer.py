score = input('成績?')
score2 = float(score)
print(type(score))
print(score)
print(type(score2))
if score2<60:
    print('不及格')
elif score2>100:
    print('不可能')
    print('一定有加分題')
elif score2>1000:
    print('你根本是亂打')
elif score2<=0:
    print('請問智商?')
else:
    print('及格')    