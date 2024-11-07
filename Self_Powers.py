serie_sum = 0

for i in range(1, 1001): # count the self powers
    serie_sum += i ** i

digits = str(serie_sum) # convert it to a string to get access to each digit

ten_last_digits = digits[-10:] # from The 10 item backward to the last digit

print(ten_last_digits)