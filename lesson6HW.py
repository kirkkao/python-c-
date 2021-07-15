k = int(input('How many Classmate?'))
score_list = []
max = -1
min = 101
max_i = 0
min_i = 0
i = 0
for i in range(k):
    name = str(input('name?'))
    score = int(input('score?'))
    score_list.append(score)
    score_list.append(name)
    print(score_list)
    print('Seat number:', i+1, 'name:', name, 'score:', score)
while i < k:
    if score_list[i*2] > max:
        max = score_list[i*2]
        max_i = i*2
    
    if score_list[i*2] < min:
        min = score_list[i*2]
        min_i = i*2
    i = i + 1
print('Highest score:',score_list[max_i],'name:',score_list[max_i+1])
print('Lowest score:',score_list[min_i],'name:',score_list[min_i+1])
print(score_list)