
def is_power_of_ten(num, power=10):
    if num==0:
        return False
    if num>=1:
        while num>1:
            num = num/float(power)
    else:
        while num<1:
            num = num*float(power)

    if num == 1:
        return True
    return False


# -------------------------------------------
# TEST CASES
# -------------------------------------------
for i in [123,100,1,10,87243,101001,234,10000000, 0.1, 0.00001, 0.0012, 0.0012, 0.001000, 0.02]:
    print i, is_power_of_ten(i)


# -------------------------------------------
# PRINT POWER of TENs WITHIN SPECIFIED RANGE
# -------------------------------------------
for i in range(0,1000000):
    i = i/1000000.0
    # print '*', i
    res = is_power_of_ten(i,10)
    if res:
        print i