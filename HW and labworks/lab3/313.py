def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


numbers = list(map(int, input().split()))

primes = list(filter(lambda x: is_prime(x), numbers))

if len(primes) > 0:
    print(*primes)
else:
    print("No primes")
