# load the 1001 * 1001 sprial
matrix = []
with open("spiral_1001x1001.txt", "r") as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

ans = 0
n = 1001

for i in range(n):
    ans += matrix[i][i]
    if not i == n//2: # revoke from adding the middle element twice
        ans += matrix[i][n-i-1]


print(ans) # 669171001

