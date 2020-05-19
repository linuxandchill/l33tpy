def is_fibonacci(i):

    history = 0, 1
    while sum(history) < i:
        history = history[1], sum(history)
    return sum(history) == i

for i in range(1, 100):
    print(is_fibonacci(i))


