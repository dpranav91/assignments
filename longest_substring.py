def find_substring(substr):
    res = ''
    for char in substr:
        if char not in res:
            res += char
        else:
            break
    # print substr, ':', res
    return res

def find_max_substring(s):
    biggest = ''
    for index in range(0,len(s)):
        substr = s[index:]
        if len(biggest)>len(substr):
            break
        res = find_substring(substr)
        if len(res)>len(biggest):
            biggest = res
    return biggest
        # yield res
