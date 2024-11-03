def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if 1 <= n < 20:
        return ones[n]
    elif 20 <= n < 100:
        return tens[n // 10] + (ones[n % 10] if n % 10 != 0 else "")
    elif 100 <= n < 1000:
        return ones[n // 100] + "hundred" + (("and" + number_to_words(n % 100)) if n % 100 != 0 else "")
    elif n == 1000:
        return "onethousand"
    return ""

def count_letters_in_words(limit):
    """Count the total number of letters from 1 to the given limit."""
    total_letters = 0
    for i in range(1, limit + 1):
        word = number_to_words(i)
        total_letters += len(word)
    return total_letters

# Calculate the total number of letters from 1 to 1000
total_letters = count_letters_in_words(1000)
print("Total number of letters from 1 to 1000:", total_letters)
