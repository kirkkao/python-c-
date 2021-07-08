print('我們來玩個猜數字遊戲。請猜 1~20之中的一個數字!!!!!!!!!!!!!!!!!!')
import random
num = float(random.randint(1, 20))
num2 = float(input('猜!'))
num3 = int(0)
if num != num2:
    print('測試結束，接下來來真的!')
else:
    print('測試結束，接下來來真的!')
while num != num2:
    num2 = float(input('猜!'))
    if num2 < num:
        print('太小了!😆😆😆')
        num3 = num3 + 1
    elif num < num2:
        print('太大了!😆😆😆')
        num3 = num3 + 1
    elif num2 > 20:
        print('請猜 1~20🤬🤬🤬')
    elif num2 < 1:
        print('請猜 1~20🤬🤬🤬')
    else:
        print('猜對了!😁😁😁')
        input('敢問高手尊姓大名?')
        print('你玩了',num3,'次')
    if num3 == int(10):
        print('失敗')
        break
if num == num2:
    print('平均',num3/10,'次猜中')