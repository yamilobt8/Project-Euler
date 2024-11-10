def is_palindrome(s):
    return s == s[::-1] # [::-1] reverse the string and return True if s == itself reversed

palindrome_sum = 0

for num in range(1, 1000000):
    if is_palindrome(str(num)): # Check if the number is palindromic in base 10
        # Check if the number is palindromic in base 2 (binary)
        if is_palindrome(bin(num)[2:]): # bin() gives '0b...' so we skip it using [2:]
            palindrome_sum += num

print(palindrome_sum)