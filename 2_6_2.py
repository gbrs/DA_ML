lst = []
for _ in range(int(input())):
    town, population = input().split()
    lst.append((int(population), town))
lst.sort()
[print(town, population) for population, town in lst]