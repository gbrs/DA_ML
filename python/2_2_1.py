lst = []
with open('titanic_train_simplified.txt') as f:
    for line in f:
        lst.append(line.strip().split(','))

# print(lst[:10])

cnt, sm = 0, 0
for i in range(1, len(lst)):
    if lst[i][5]:
        cnt += 1
        sm += float(lst[i][5])

print(sm / cnt)
