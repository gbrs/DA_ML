lst = []
with open('moscow_schools_winners.txt', encoding='utf-8') as f:
    for line in f:
        lst.append(line.split(','))

cnt = 0
for line in lst[1:]:
    if line[-6] == '4' and line[-4] == 'Математика' and line[-3] == 'победитель':
        cnt += 1

print(cnt)
