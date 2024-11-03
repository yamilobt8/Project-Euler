# pset 1
numbers = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(int(i))
    pass
sum = sum(numbers)
print(f'the sum of all multiples of 3 or 5 below 1000 is: {sum}')

