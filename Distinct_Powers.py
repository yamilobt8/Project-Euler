sequence = []

for a in range(2, 101): # for each a between 2 and 101
    for b in range(2, 101): # we combine it with b in the same range
        combination = a ** b
        if combination not in sequence: # To make the terms distinct
            sequence.append(combination)

n = len(sequence)
print(n) # 9183