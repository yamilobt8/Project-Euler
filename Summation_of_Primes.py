import math

def is_prime(number):
    if number <= 1:
        return False
    if number in [2, 3]:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

limit = int(input('entre The limit: ')) # in our case 2000000
primes_summation = 0

for i in range(2, limit):
    if is_prime(i):
        primes_summation += i
print(primes_summation)