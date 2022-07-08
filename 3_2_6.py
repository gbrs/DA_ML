lst = []
with open('1.csv') as f:
    for line in f:
        lst.append(line.strip().split(','))

# print(lst)

col = lst[0].index('a')
sm = 0
cnt = 0
for i in range(1, len(lst)):
    if lst[i][col]:
        sm += float(lst[i][col])
        cnt += 1

answer = round((sm + 0.0001) / cnt)

print(answer)
