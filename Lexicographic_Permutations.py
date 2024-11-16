def permutations(arrangement):
    if len(arrangement) == 1:
        return [arrangement]
    
    result = [] # a list where we can store permutations
    for i in range(len(arrangement)): # Loop over The arrangement List
        base = arrangement[i] # Fix a number
        rest = arrangement[:i] + arrangement[i + 1:] # Get the rest of numbers so we can use recursion on them
        permutations_of_rest = permutations(rest) # Getting The Possible arrangements of the rest
        for perm in permutations_of_rest: # Adding The Base we fixed To The permutations Generated
            result.append([base] + perm)
    return result
        



arrangement = [0, 1 ,2, 3, 4, 5, 6, 7, 8 , 9]

arrangement_permutations = permutations(arrangement) # A list Contains All The Permutations Generated

# Find the 1,000,000th permutation (index 999,999 in 0-based indexing)
millionth_permutation = arrangement_permutations[999999]
millionth_permutation_string = ''.join(map(str, millionth_permutation)) # Convert the list to a string to make it readable

print(millionth_permutation_string)