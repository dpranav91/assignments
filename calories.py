'''
PROBLEM:
--------

There are three different types (t1, t2, t3) of fruits each giving 2,3,7 calories respectively.
Cost and quantity in which we could purchase for each fruit will be provided as input
along with Total calories required. Find the fruits combination that results out in
least price on buying such combination. Return Least Cost as result.


INPUT:
-------
COSTS : 4, 5, 2
QUANTITIES : 3, 2, 5
TOTAL CALORIES REQUIRED TO MAKE : 47

RESULT:
-------
LEAST SUM : 32

SOLUTION:
---------
On buying: 3 t1, 2 t2 and 5 t3 you can make 74 calories,
so total cost will be (3 * 4) + (2 * 5) + (5 * 2)= 32
'''

from itertools import product


def least_amount_to_obtain_s_calories(calories, quantities, costs, calories_count):
    get_possibilities = lambda calorie, quantity: [calorie * i for i in range(quantity + 1) if calorie * i < calories_count]

    # list of all possibilities for each of the calorie type
    possibilities = [get_possibilities(calories[index], quantities[index]) for index in range(len(calories))]

    # least to be to set to MAX value, so as to compare later
    least_cost = float('inf')

    # get all the possible collections by performing itertools.product on possibilities
    for each_combination in product(*possibilities):
        if sum(each_combination) == calories_count:
            print(each_combination)
            each_combination_prices = [(j / calories[index]) * costs[index] if j != 0 else 0 for index, j in
                                       enumerate(each_combination)]
            combination_cost = (sum(each_combination_prices))

            # store least cost by comparing cost for each combination
            if combination_cost < least_cost:
                least_cost = combination_cost
    return least_cost


if __name__ == '__main__':
    res = least_amount_to_obtain_s_calories(calories=[2, 3, 7],
                                            quantities=[3, 2, 5],
                                            costs=[4, 5, 2],
                                            calories_count=47)
    # combinations([[1,2], [11,22], [111,222]])
    print(res)
