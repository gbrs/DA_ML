def gen_fib(n):
    lst = [1, 1, 2]
    for i in range(3, n):
        lst.append(lst[-2] + lst[-1])
    return lst


print(*gen_fib(3))
