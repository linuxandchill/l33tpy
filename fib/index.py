##  returns the nth number in the fib sequence
cache = {}

def fib(n):
    if n in cache:
        return cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n-2) + fib(n-1)

    cache[n] = value
    return value
    


print(fib(70))