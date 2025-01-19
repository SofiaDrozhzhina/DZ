def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


def golden_ratio(i):
    fib_i = fibonacci(i)
    fib_i_plus_1 = fibonacci(i + 1)
    goldratio = fib_i_plus_1 / fib_i
    print(goldratio)


