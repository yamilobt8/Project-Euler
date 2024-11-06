def collatz_length(n, memo):
    if n in memo:
        return memo[n]
    
    if n == 1:
        return 1
    
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    
    length = 1 + collatz_length(next_n, memo)
    memo[n] = length
    return length

def longest_collatz_chain(limit):
    longest_chain = 0
    best_starting_number = 0
    memo = {}

    for starting_number in range(1, limit):
        current_chain = collatz_length(starting_number, memo)
        if current_chain > longest_chain:
            longest_chain = current_chain
            best_starting_number = starting_number

    return best_starting_number, longest_chain

result = longest_collatz_chain(1000000)
print(f"The longest chain is {result[1]} for starting number {result[0]}.")
# end