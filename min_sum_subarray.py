'''
MINIMUM SUM SUBLIST
---------------------

Write function mssl() (minimum sum sublist) that takes as input a list of integers.
It then computes and returns the sum of the maximum sum sublist of the input list.
The maximum sum sublist is a sublist (slice) of the input list whose sum of entries is largest.
The empty sublist is defined to have sum 0.
For example, the maximum sum sublist of the
list [4, -2, -8, 5, -2, 7, 7, 2, -6, 5] is [5, -2, 7, 7, 2] and the sum of its entries is 19
'''

# GENERAL PROGRAM
from collections import defaultdict

def mssl_1(lst, return_sublist=False):
    d = defaultdict(list)
    for i in range(len(lst)+1):
        for j in range(i+1,len(lst)+1):
            d[sum(lst[i:j])].append(lst[i:j])
    key = max(d.keys())
    if return_sublist:
        return (key, d[key])
    return key


# DYNAMIC PROGRAMMING
def mssl_2(l):

    best = cur = 0
    start = end = 0
    for index, num in enumerate(l):
        cur = max(cur + num, 0)
        if cur <= 0 and start <= end:
            start = index
        if cur < best:
            end = index

        if start and end:
            print l[start+1:end]
        best = max(best, cur)
    return best, l[start:end]

if __name__ == '__main__':
    print (mssl_1([4, 2, -8, 5, -2, 7, 7, 2, -6, -15, 6, -2]))
    print (mssl_2([4, 2, -8, 5, -2, 7, 7, 2, -6, -15, 6, -2]))