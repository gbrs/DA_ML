N = int(input())
sm = cnt = 0
for i in range(2, N + 1):
    for j in range(2, int(i**0.5 + 1)):
        if not i % j:
            break
    else:
        sm += i
        cnt += 1
print(round((sm + 0.0001) / cnt, 2))
