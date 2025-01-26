# A number chain is created by continuously adding the square of the digits in a number 
# to form a new number until it has been seen before.
# 
# For example:
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
# 
# Therefore, any chain that arrives at 1 or 89 will become stuck in an endless loop.
# What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
# 
# How many starting numbers below ten million will arrive at 89?

ans = 0 

num = 10000000 #runtime: 1m 45s

while num > 1:
    
    sequence = [num]
    i = 0
    while True:
        next_item = sum(int(digit) ** 2 for digit in str(sequence[i]))    
        if next_item == 1:
            break
        if next_item == 89:
            ans += 1
            break
        else:
            sequence.append(next_item)
            i += 1
    num -= 1
        
print(ans) # 8581146
    
    