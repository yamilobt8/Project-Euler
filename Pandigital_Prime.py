def is_prime(n): # function to check prime numbers
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def are_consecutives(list): # function to see if the numbers are consecutives like (12354)
    for i in range(len(list) - 1):
        if list[i] + 1 != list[i + 1]: # for example: [1, 2, 3, 5] we compare each digit with the next one
            return False
    return True

n = 0
number = 0
for num in range(2, 7652415): # instead of looping over 10000000 we loop over 7652415 to reduce run time
    if is_prime(num):
        digits = sorted([int(digit) for digit in str(num)]) # we sort the array after appending the number digits
        if digits[0] == 1: # if the sorted number start with 1
            if are_consecutives(digits) and max(digits) >= n:
                n = max(digits)
                number = num

print(n) # 1 --> n 
print(number) # 7652413

