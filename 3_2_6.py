lst = []
with open('1.csv') as f:
    for line in f:
        lst.append(line.strip().replace(',', ' ').split())

# print(lst)

col = lst[0].index('a')
sm = 0
for i in range(1, len(lst)):
    sm += float(lst[i][col])

print(round((sm + 0.0001) / (len(lst) - 1)))
