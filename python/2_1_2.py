N = int(input())
lst = list(map(float, input().split()))
answer = []
answer.append(lst[0])
for i in range(N-2):
    answer.append(sum(lst[i:i + 3]) / 3)
answer.append(lst[-1])
print(*answer)
