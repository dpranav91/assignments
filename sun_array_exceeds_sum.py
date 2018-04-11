# Problem Name is &&& SubArray Exceeding Sum &&& PLEASE DO NOT REMOVE THIS LINE.

"""
 Instructions to candidate.
  1) Your task is ultimately to implement a function that takes in an array of non-negative numbers and an integer.
     You want to return the *LENGTH* of the shortest subarray whose sum is at least the integer,
     and -1 if no such sum exists.
  2) Run this code in the REPL to observe its behaviour. The
     execution entry point is main().
  3) Consider adding some additional tests in doTestsPass().
  4) Implement subArrayExceedsSum() correctly.
  5) If time permits, some possible follow-ups.
"""
import pdb


def subArrayExceedsSum(arr, target):
    # todo: implement here

    # 1 2 3,
    # 2 3 4, 2 4,
    # 3 4

    res = []
    arr_len = len(arr)
    for i in range(arr_len):
        init_num = arr[i]
        sub_res = [init_num]
        if sum(sub_res) >= target:
            res.append(sub_res)
            continue
        for j in range(i + 1, arr_len):
            sub_res.append(arr[j])

            if sum(sub_res) >= target:
                res.append(sub_res)
                break
            # sub_res.append(arr[j])

    if res:
        return res, min(map(lambda x: len(x), res))
    else:
        return -1


def doTestsPass():
    """ Returns 1 if all tests pass. Otherwise returns 0. """
    testArrays = [[[1, 2, 3, 4], 6], [[1, 2, 3, 4], 12]]
    testAnswers = [2, -1]

    for i in range(len(testArrays)):
        print (subArrayExceedsSum(testArrays[i][0], testArrays[i][1]), testAnswers[i])
        if not (subArrayExceedsSum(testArrays[i][0], testArrays[i][1]) == testAnswers[i]):
            return False

    return True


if __name__ == "__main__":
    if (doTestsPass()):
        print("All tests pass")
    else:
        print("Not all tests pass")
