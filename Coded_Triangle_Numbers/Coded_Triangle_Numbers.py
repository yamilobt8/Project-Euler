from math import isqrt

def is_trangular(n):
    check_value = 8 * n + 1 # we will check for this value if its a perfect square
    sqrt_val = int(isqrt(check_value)) # find the root square of the check value
    if sqrt_val * sqrt_val == check_value: # if yes then its a perfect square
        return (sqrt_val - 1) % 2 == 0 # if this value is even , means n is an integer 
    return False

def alphabetical_position(char):
    char = char.lower()
    return ord(char) - 96

triangle_words = 0

with open('0042words.txt', 'r') as words:
    names = words.read().replace('"', '').split(',')
    for name in names: # we loop over each name
        word_value = 0
        for char in name: # we loop over each char in the name
            word_value += alphabetical_position(char) # we incrment the word value by the charposition
        if is_trangular(word_value): # if the score is trangular we add one to the triangle_words
            triangle_words += 1
    
print(triangle_words) # 162
        
