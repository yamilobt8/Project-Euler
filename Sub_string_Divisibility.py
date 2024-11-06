pandijital_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # the possible digits that can be on the number

def generate_permutations(elements): # generate the numbers based on the list above
    if len(elements) == 1:
        return [elements]
    
    permutations = []
    for i in range(len(elements)):
        current = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        for perm in generate_permutations(remaining_elements): # using recursion to get all the possible numbers(order)
            permutations.append([current] + perm)
    return permutations

def check_property(n): # checking for divisibility 
    return (int(n[1:4]) % 2 == 0 and    # d2d3d4 is divisible by 2 
            int(n[2:5]) % 3 == 0 and    # d3d4d5 is divisible by 3
            int(n[3:6]) % 5 == 0 and    # d4d5d6 is divisible by 5
            int(n[4:7]) % 7 == 0 and    # d5d6d7 is divisible by 7
            int(n[5:8]) % 11 == 0 and   # d6d7d8 is divisible by 11
            int(n[6:9]) % 13 == 0 and   # d7d8d9 is divisible by 13
            int(n[7:10]) % 17 == 0)     # d8d9d10 is divisible by 17


pandijital_number_sum = 0
 
all_permutations = generate_permutations(pandijital_number)

all_possible_numbers = [int(''.join(map(str, perm))) for perm in all_permutations] # grouping permutations


for number in all_possible_numbers: # looping over the pandijital_number list
    if check_property(str(number)):
        pandijital_number_sum += number

print(pandijital_number_sum) # 16695334890