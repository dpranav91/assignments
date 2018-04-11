'''
PROBLEM:
--------
Given COINS as an array; and total amount to be made as S (integer)
FInd total number of ways in which a TOTAL of S amount could be made using the given COINS base


INPUT:
-------
COINS: 3, 5, 7
S: 20

RESULT:
-------
COMBINATIONS : 4

SOLUTION:
---------
4 ways of making 20 using coins (3, 5, 7):
{3, 3, 3, 3, 3, 5}
{3, 3, 7, 7}
{3, 5, 5, 7}
{5, 5, 5, 5}
'''


def coins_change_combinations(coins, amount):
    # Using DYNAMIC PROGRAMMING, to store total combinations for each value until total amount needs to be found

    # We are going to store number of ways in which certain number could be formed, using all the coins,
    # for each integer starting from number 1 to amount in result array

    # first value of result array will have to be 1, as we could make amount X value using coin X, only in one way;
    # i.e., considering X as 5, Amount 5 could be made by coin 5 only in one way
    # and rest of the values will be set to 0 initially
    result = [1] + [0] * amount

    # for each coin; iterate over range of integers until amount and find out
    # the numbers of ways in which each number could be made using all coins
    # and store in result array
    for coin in coins:
        # ignore if sub_amount is is lesser than coin value
        # so considering the range to be starting from coin value
        for sub_amount in range(coin, amount + 1):
            result[sub_amount] += result[sub_amount - coin]
    return result[amount]


if __name__ == '__main__':
    amount = 20
    coins = [3, 5, 7]
    print(coins_change_combinations(coins, amount))
