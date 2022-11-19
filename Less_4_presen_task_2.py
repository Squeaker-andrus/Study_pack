def factor(n:int) -> int:
    if n < 1:
        return 1
    return n * factor(n - 1)

print(factor(4))