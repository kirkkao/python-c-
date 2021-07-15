i = input('A同學成績?')
j = input('B同學成績?')
k = input('C同學成績?')
l = input('D同學成績?')
score2 = [i,j,k,l]
a = score2[0]
b = score2[1]
c = score2[2]
d = score2[3]
print(score2)
if a > b and a > c and a > d:
    print('A最高')
elif b > a and b > c and b > d:
    print('B最高')
elif c > a and c > b and c > d:
    print('C最高')
elif d > a and d > b and d > c:
    print('D最高')
if a < b and a < c and a < d:
    print('A最低')
elif b < a and b < c and b < d:
    print('B最低')
elif c < a and c < b and c < d:
    print('C最低')
elif d < a and d < b and d < c:
    print('D最低')