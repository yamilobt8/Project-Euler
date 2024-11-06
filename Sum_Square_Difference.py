def get_squares_sum(number):
    square_sum = 0
    for i in range(1, number + 1):
        square_sum += i ** 2
    return square_sum

def get_sum_square(number):
    sum_square = 0
    for i in range(1, number + 1):
        sum_square += i
    return sum_square ** 2

number = int(input('entre the number: ')) # in our case 100
square_sum = get_squares_sum(number)
sum_square = get_sum_square(number)

print(f'Diff: {sum_square - square_sum}')
# end