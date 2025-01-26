""" 
A googol (10 ** 100) is a massive number: one followed by one-hundred zeros; 100 * 100 is almost unimaginably large: 
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a ** b, where a, b < 100, what is the maximum digital sum?
"""

a = 100

digital_sum = 0

while a > 1:
    b = a
    while b > 1:
        result = str(a ** b)
        digital_sum = max(sum(int(digit) for digit in result), digital_sum)
        b -= 1
    a -= 1
        
        
print(digital_sum)
    