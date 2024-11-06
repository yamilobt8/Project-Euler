import math

def count_divisors(x):
    divisors = 0
    root = int(math.sqrt(x))
    for i in range(1, root + 1):
        if x % i == 0:
            divisors += 2 if i != x // i else 1
    return divisors

def find_triangle_number(limit):
    n = 1
    while True:
        triangle_number = n * (n + 1) // 2
        if n % 2 == 0:
            divisors = count_divisors(n // 2) * count_divisors(n + 1)
        else:
            divisors = count_divisors(n) * count_divisors((n + 1) // 2)
        if divisors > limit:
            return triangle_number
        n += 1

number = find_triangle_number(500) # in our case 500
print(number)
# end