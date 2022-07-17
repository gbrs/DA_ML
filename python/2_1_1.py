n, k = map(int, input().split())
old = 0
yang = 1
for i in range(1, n):
    old, yang = old + yang, old * k

print(old + yang)
