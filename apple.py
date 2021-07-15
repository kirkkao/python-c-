o = int(input('有多少蘋果?'))
a = int(input('要使用什麼功能?'))    
p = int(2)
for t in range(1, p):
    if a == 1:
        p = p + 1
        k = int(input('一個蘋果多少錢?'))
        i = int(input('今天賣了多少個蘋果?'))
        print('應得',k * i,'元')
        a = int(input('要使用什麼功能?')) 
    elif a == 2:
        p = p + 1
        i = int(input('進貨了幾個蘋果?'))
        print('目前庫存有',o + i,'個蘋果')
        o = o + i
        a = int(input('要使用什麼功能?')) 
    elif a == 3:
        p = p + 1
        t = int(input('出貨多少蘋果?'))
        print('目前庫存有', o - t, '個蘋果')
        o = o - t
        a = int(input('要使用什麼功能?'))
    else:
        print('服務代碼錯誤')
        p = 1