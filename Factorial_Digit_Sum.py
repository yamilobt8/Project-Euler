def factorial(n): # using recursion to calculate recursion
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(input('entre n!: ')) # in our case 100
result = str(factorial(n)).replace('0', '') # deleting 0's from the result to reduce time complexity
factorial_sum = 0
for i in range(len(result)):
    factorial_sum += int(result[i])
print(factorial_sum)
# end