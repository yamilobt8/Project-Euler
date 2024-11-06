# Note: The runtime may take some minutes check the optimized version
def is_even(n):
    return n % 2 == 0

starting_number = 0
longest_chain = 0
best_starting_number = 0

while starting_number < 1000000:
    current_item = starting_number
    current_chain = 0

    while current_item != 1:
        if is_even(current_item):
            current_item = current_item // 2
        else:
            current_item = 3 * current_item + 1
        current_chain += 1

    # Check if the current chain is the longest
    if current_chain > longest_chain:
        longest_chain = current_chain
        best_starting_number = starting_number

    starting_number += 1

print(f"The longest chain is {longest_chain} for starting number {best_starting_number}.")
# end