# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

found = False

multiples = [3, 4, 5, 6]

x = 1

while not found:
    found = True # if wee didn't change the boolean value of it it will break automatically
    digits = sorted([digit for digit in str(x * 2)]) # sort the digit of 2x
    for multiple in multiples:
        
        if sorted([i for i in str(x * multiple)]) != digits: # check the digits of the digits of 3x, 4x, 5x, 6x with the base 2x
            found = False # if only one don't satisfie quit
            break
    if not found:
        x += 1
    
    
    
print(x)