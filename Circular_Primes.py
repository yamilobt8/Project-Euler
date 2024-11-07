def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(2, 1000000):
    if is_prime(i):
        primes.append(i)
    

def is_circular(n):
    digits = str(n) # convert The Prime n to a string so we can reach each digit individually

    for i in range(len(digits)):
        rotated = int(digits[i:] + digits[:i])
        if not is_prime(rotated):
            return False
    return True


circular_primes = []
for prime in primes:
    if is_circular(prime):
        circular_primes.append(prime)

circular_primes_quantity = len(circular_primes)

print(circular_primes_quantity) # 55
