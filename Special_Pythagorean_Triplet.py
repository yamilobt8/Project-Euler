def find_pythagorean_triplets(sum_total):
    for a in range(1, sum_total // 3): # reduce time complexity by reducing the loop end (a < b)
        for b in range(a + 1, sum_total // 2): # b != a and b > a
            c = sum_total - a - b # a + b + c = 1000 -> c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c # return the product abc
    return 0

triplet = find_pythagorean_triplets(1000)
print(triplet) # 31875000
# end