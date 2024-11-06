# pset2
def fibonacci(limit):
    a, b = 1, 2
    sum = 0

    while a <= limit:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
    return sum
result = fibonacci(4000000)
print(f"The sum of even-valued Fibonacci terms not exceeding 4 million is: {result}")
# end