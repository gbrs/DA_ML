def is_perfect(n):
    sm = 0
    for i in range(1, n):
        if n % i == 0:
            sm += i
    if sm == n:
        return True
    return False


print(is_perfect(8128))
