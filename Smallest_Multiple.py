smallest_number = 2520 # Starting Point

while True:
    for i in range(1, 21): # Looping on The divisable numbers
        if smallest_number % i != 0: # checking if there is any remainder
            break
    else:
        break
    smallest_number += 20 # increasing the number by 20 to reduct time complexity

print(smallest_number)
# end