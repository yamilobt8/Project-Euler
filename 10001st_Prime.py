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

def find_nth_prime(number):
    count, num = 0, 1
    while count < number: # We didn't Find nth prime numbers yet
        num += 1
        if is_prime(num):
            count += 1
    return num # we exit the loop after finding the nth prime and return it

number = int(input('entre The nth Prime you would like to see: '))
print(find_nth_prime(number))