lst = []
with open('earthquakes.txt') as f:
    for line in f:
        lst.append(line.strip().split(','))
for line in lst[1:]:
    line[1] = float(line[1])
print(sorted(lst[1:], key=lambda x: x[1])[-1][0])
