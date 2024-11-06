# pset 4

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product > largest:
                largest = product
    return largest

print(largest_palindrome())
# end