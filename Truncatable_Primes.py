def is_prime(n): # function to check prime numbers
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncable_left_to_right(digits):
    # Check if truncating from left to right always yields a prime
    for i in range(len(digits)):
        number = int(''.join(map(str, digits[i:])))
        if not is_prime(number):
            return False
    return True

def is_truncable_right_to_left(digits):
    # Check if truncating from right to left always yields a prime
    for i in range(len(digits)):
        number = int(''.join(map(str, digits[:len(digits) - i])))
        if not is_prime(number):
            return False
    return True

truncable_primes_sum = 0
truncable_primes_count = 0

i = 10
while truncable_primes_count < 11:
    if is_prime(i):
        digits = [int(digit) for digit in str(i)]
        reversed_digits = list(reversed(digits))
        if is_truncable_left_to_right(digits) and is_truncable_right_to_left(digits):
            truncable_primes_count += 1
            truncable_primes_sum += i
    i += 1

print(truncable_primes_sum) # 748317