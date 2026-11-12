def factorial_recersive(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial_recersive(n-1)

print(factorial_recersive(7))
