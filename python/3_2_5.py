output = []

for _ in range(int(input())):
    s = input()
    if s.isalpha():
        output.append(s)

print(*output, sep=', ')
