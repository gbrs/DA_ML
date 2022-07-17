def is_simple(n):
    if n < 3:
        return True
    for i in range(2, int(n ** 0.5) + 2):
        if n % i == 0:
            return False
    return True


print(is_simple(997))
