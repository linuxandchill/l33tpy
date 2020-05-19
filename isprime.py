def is_prime(n):
    return all(n % j  for j in range(2, n))

print(is_prime(10))
