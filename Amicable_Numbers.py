def found_amicable_numbers(limit):
    amicable_numbers = []
    for a in range(2, limit):
        b = find_divisors(a)
        if b != a and find_divisors(b) == a: # checking for d(a) = b and d(b) = a
            amicable_numbers.extend([a, b])
    return sum(set(amicable_numbers)) # using set to avoid duplicates

def find_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

sum_of_amicable_numbers = found_amicable_numbers(10000)

print(sum_of_amicable_numbers) # 31626