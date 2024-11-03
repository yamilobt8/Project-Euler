# pset 3
def largest_factor(n):
    factor = 2
    while n > 1:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return factor
result = largest_factor(600851475143)
print(f"The largest prime factor of 600851475143 is: {result}")