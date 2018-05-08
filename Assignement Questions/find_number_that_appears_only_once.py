'''
Find the number in a list that appears only once, whereas rest of the numbers repeats thrice.
NOTE: SHOULD NOT USE ADDITIONAL "MEMORY SPACE" AND ALGORITHM SHOULD BE "O(n)"

 Example :
 ---------
 INPUT: [2,3,4,2,3,4,4,3,2,1,5,6,5,5,6,6]
 OUTPUT : 1
 REASON: 2,3,4,5,6 appears thrice, but only 1 appears once

'''

def find_number_that_appears_only_once(array):
    binaries = [str(int(bin(item)[2:])).zfill(10) for item in array]
    binaries_sum = [sum(map(int, i))%3 for i in zip(*binaries)]
    print binaries_sum

    res = ''.join(str(item) for item in binaries_sum)

    print res, eval('0b'+res)
    return eval('0b'+res)




def test():
    test_cases = [
        ([1,2,2,2,3,3,3,4,4,5,5,5,4], 1),
        ([1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 4], 2),
        ([1, 1, 1, 21, 3, 3, 3, 51, 51, 51, 3 ,3 , 3, 44, 44, 44], 21)
    ]
    result = True
    for test_case, expected in test_cases:
        actual = find_number_that_appears_only_once(test_case)
        if actual != expected:
            print ("TEST CASE FAILED\nInput: {}\nExpected:{}\nActual:{}\n".format(test_case, expected, actual))
            result = False
    return result

if __name__ == '__main__':
    test()
