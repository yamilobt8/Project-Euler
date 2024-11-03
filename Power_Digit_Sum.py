number = str(2 ** 1000) # converting the number to a string so we can get his lenght
digits_sum = 0 
for i in range(len(number)): # loop over the number digits
    digits_sum += int(number[i]) 

print(digits_sum)
