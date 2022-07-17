n, m = map(int, input().split())
old = [0] * (m - 1)  # стек
yang = [1]
for i in range(1, n):
    yang.append(1 * sum(old))
    old.pop(0)
    old.append(yang[-2])

# print(*old)
# print(*yang)
print(sum(old) + yang[-1])
