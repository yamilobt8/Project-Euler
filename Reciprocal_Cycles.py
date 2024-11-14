max_cycle_length = 0
max_value = 0

for d in range(2, 1000):
    remainders = {}
    value = 1
    position = 0

    while value != 0:
        if value in remainders:
            cycle_length = position - remainders[value]
            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length
                max_value = d
            break

        remainders[value] = position

        value = (value * 10) % d
        position += 1

print(max_value) # 983
print(max_cycle_length) # 982