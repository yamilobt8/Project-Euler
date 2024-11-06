a, b = 1, 1 # initialize first 2 fibonacci numbers
index = 2

while len(str(b)) < 1000:
    a, b = b, a + b # update the Fibonacci sequence
    index += 1

print(index) # 4782
# end