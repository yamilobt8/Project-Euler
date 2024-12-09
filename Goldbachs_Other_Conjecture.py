import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_composite(n):
    return n > 1 and not is_prime(n)

def sum_of_prime_and_twice_a_square(n):
    for p in range(2, n):
        if is_prime(p):
            for k in range(1, int(math.sqrt(n // 2)) + 1):
                if p + 2 * (k ** 2) == n:
                    return True
    return False

odd = 9

while True:
    if is_composite(odd) and not sum_of_prime_and_twice_a_square(odd):
        break
    odd += 2

print(odd) # 5777