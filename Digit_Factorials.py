def factorial(n):
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)
    
def sum_of_digit_factorials(n):
    return sum(factorial(int(digit)) for digit in str(n))

curios_numbers_sum = 0

for i in range(3, 1000000): # Limit it on 1m
    if sum_of_digit_factorials(i) == i:
        curios_numbers_sum += i

print(curios_numbers_sum) # 40730
