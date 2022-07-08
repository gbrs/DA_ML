lst = []
with open('titanic_train_simplified.txt') as f:
    for line in f:
        lst.append(line.strip().split(','))

# print(lst[:10])

cnt1 = cnt2 = cnt3 = 0
for i in range(1, len(lst)):
    if lst[i][2] == '3':
        cnt3 += 1
    elif lst[i][2] == '2':
        cnt2 += 1
    elif lst[i][2] == '1':
        cnt1 +=1

print(cnt1, cnt2, cnt3)
