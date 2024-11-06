def check(n):
    return sum(int(digit) ** 5 for digit in n) == int(n) # checking if the sum of digits * 5 equal to the number

numbers_sum = 0
for i in range(2, 354295): # 9 ** 5 = 59049 and 59049 * 6 = 354295
    if check(str(i)):
        numbers_sum += int(i)

print(numbers_sum) # 443839