def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, limit + 1, current):
                sieve[multiple] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

limit = 2000000
primes = sieve_of_eratosthenes(limit)
summation = sum(primes)

print(f"Sum of prime numbers below {limit}: {summation}")
