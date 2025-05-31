coins = [1, 2, 5, 10, 20, 50, 100, 200]


def coin_sums(target, coins):
    if len(coins) == 1:
        return 1 if target % coins[0] == 0 else 0
    
    choice = coins[0]
    ans = 0
    n = 0
    
    while choice * n <= target:
        remaining = target - choice * n
        ans += coin_sums(remaining, coins[1:])
        n += 1
    
    return ans

print(coin_sums(200, coins[::-1])) # 73682