'''
For each item in list, get the next occuring greater number (to the right) and form a list.
If there isnt any greater element, value should be -1.

NOTE: ALGORITHM SHOULD BE "O(n)" AND NO RESTRICTION ON MEMORY SPACE

Example:
INPUT: [5,4,6,2,3,7,9]
OUTPUT: [6,6,7,3,7,-1]

'''


def next_greater_item_list(num_list):
    result = []
    # iterate over each element of list
    for elem in num_list:
        # inintially result for each item will be set to [element, -1]
        # -1 is default value for result
        result.append([elem,-1])

        # iterate over result in reverse manner (ignore iterating recetn element)
        for i in result[::-1][1:]:
            # if element is greater than each item index-0, -1 will be set to elem
            if i[1] == -1 and i[0] < elem:
                i[1] = elem
    # finally consider only index-1 of the result
    return [i[1] for i in result]


def test():
    test_cases = [
        ([5, 4, 6, 2, 3, 7, 9], [6, 6, 7, 3, 7, 9, -1]),
        ([1, 4, 6, 2, 3, 8, 5], [4, 6, 8, 3, 8, -1, -1]),
        ([1, 4, 1, 2, 10, 8, 5], [4, 10, 2, 10, -1, -1, -1]),
        ([5, 4, 3, 2, 10], [10, 10, 10, 10, -1]),
    ]
    result = True
    for test_case, expected in test_cases:
        actual = next_greater_item_list(test_case)
        if actual != expected:
            print ("TEST CASE FAILED\nInput: {}\nExpected:{}\nActual:{}\n".format(test_case, expected, actual))
            result = False
    return result

if __name__ == '__main__':
    print (test())
