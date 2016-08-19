def fib(n):
    """comment"""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    print()
    return result

print(fib(2000))    