def split_pairs(s):
    if len(s) % 2 > 0:
        s+='_'
    pair1, pair2 = s[:len(s)//2], s[len(s)//2:]
    return [pair1, pair2]


def max_triple(array):
    max = 0
    for i in range(len(array)-2):
        if array[i] + array[i+1] + array[i+2] > max:
            max = array[i] + array[i+1] + array[i+2]
            max_tup = (array[i], array[i+1], array[i+2])
    return max_tup

def check(password):
    symb = '!@#$%^&*()_+,./<>|\"£^&'
    criteria_symb = 0
    criteria_alpha = 0
    criteria_digit = 0
    criteria_upper = 0
    criteria_lower = 0
    if len(password) > 8:
        for e in password:
            if e.isupper():
                criteria_upper += 1
            if e.islower():
                criteria_lower += 1
            if e.isdigit():
                criteria_digit += 1
            if e.isalpha():
                criteria_alpha += 1
            if e in symb:
                criteria_symb += 1
    else:
        return False
    return True if (criteria_alpha >= 2 and criteria_upper >= 2
                    and criteria_lower >= 2 and criteria_digit >= 2
                    and criteria_symb >= 2) else False

def merge(*args):
    dic = {}
    for e in args:
        last = []
        for k, v in e.items():
            dic[k] = v
            if k in dic:
                last.append(v)
                dic[k] = last
    return dic

a = {1:2, 3:4}
b = {1:10, 2:5, 7:10}
c = {1:7, 2:10}

print(merge(a,b,c))