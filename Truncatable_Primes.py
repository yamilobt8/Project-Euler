def is_prime(n): # function to check prime numbers
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

truncable_primes_sum = 0
truncable_primes_count = 0

def is_truncable(digits):
    left_and_right = 0
    # truncate digits from left
    for i in range(len(digits)):
        number = int(''.join(map(str, digits[i:])))
        if not is_prime(number):
            return False
    left_and_right += 1

    digits = list(reversed(digits)) # we reverse the list so we can try truncate from the right
    # truncate digits from right
    for j in range(len(digits)):
        number = int(''.join(map(str, digits[j:])))
        if not is_prime(number):
            return False
    left_and_right += 1

i = 8
while truncable_primes_count < 2:
    if is_prime(i):
        digits = [int(digit) for digit in str(i)]
        if is_truncable(digits):
            truncable_primes_count += 1
            truncable_primes_sum += i

    i += 1

print(truncable_primes_sum)
print(truncable_primes_count)