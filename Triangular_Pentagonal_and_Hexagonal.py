import math

def is_pentagonal(x):
    n = (1 + math.sqrt(1 + 24 * x)) / 6
    return n.is_integer() # it return True if n is int else return False

n = 144 # Start From The next hexagonal number after H_143

while True:
    
    hexagonal = n * (2 * n - 1)
    if is_pentagonal(hexagonal):
        break

    n += 1

print(hexagonal)
