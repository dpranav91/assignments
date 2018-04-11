# -*- coding: utf-8 -*-

# T: an array containing the values of the coins
# L: integer which is the total to give back
# Output: Minimal number of coins needed to make a total of L
def dynamicCoinChange(coins, total_sum):
    result = [0] * (total_sum + 1)

    for num in range(1, total_sum + 1):
        smallest = float("inf")
        for coin in coins:
            if coin <= num:
                smallest = min(smallest, result[num - coin])
        result[num] = 1 + smallest
    return result[total_sum]


# Coin change situations
problems = [
    # [[1, 5, 10, 20, 50, 100, 200],  10000000],
    [[1, 3, 4], 20],
    [[1, 2, 3], 9],
    [[1, 2, 3], 10],
    [[1, 5], 13923],
    [[7, 22, 71, 231], 753],
    [[3, 5, 12], 25],
    [[800], 800],
    [[2], 50000]
]

# Test Loop
for T, L in problems:
    S = dynamicCoinChange(T, L)
    # print ("dynamicCoinChange(T, L)")
    print("T =", T)
    print("L =", L)
    print("Answer =", S)
