def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# generate a list of primes below our limite in our case 1m
def generate_primes(limit):
    primes = []
    for i in range(2, limit):
        if is_prime(i):
            primes.append(i)
    return primes       

def find_largest_prime_sum(limit):
    primes = generate_primes(limit)
    max_prime = 0
    max_lenght = 0

    for i in range(len(primes)):
        current_sum = 0
        for j in range(i, len(primes)):
            current_sum += primes[j]

            if current_sum >= limit:
                break

            if is_prime(current_sum) and (j - i + 1) > max_lenght:
                max_lenght = j - i + 1
                max_prime = current_sum
    return max_prime
        

limit = int(input('entrez la limite des primes: ')) # in our case 1m

print(find_largest_prime_sum(limit))