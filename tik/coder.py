from collections import OrderedDict


def bwt(some_string):
    a = list(some_string)
    letters = []
    [(a.append(a.pop(0)), letters.append(a[:])) for i in range(len(a))]
    letters.sort()
    result = ''.join([e[-1] for e in letters])
    return result, letters.index(a)


def get_string():
    with open('file.txt', 'r') as f:
        return f.readlines()[0]


def to_bin(digit):
    result = ''
    while digit > 0:
        result += str(digit % 2)
        digit //= 2
    result = '0' * (8 - len(result)) + result[::-1]
    return result


def lzw(some_string):
    output = ''
    sdvig = 1
    k = 0
    s = 1

    while k + s < len(some_string) * 2:
        if (x := some_string[k:s]) not in my_dict:
            my_dict[x] = len(my_dict) + 1
            output += str(to_bin(my_dict[some_string[k:s-1]]))
            k += sdvig - 1
            sdvig = 1
        else:
            s += 1
            sdvig += 1

    output += str(to_bin(my_dict[string[k:s-1]]))
    return output


string = get_string()
string, ind = bwt(string)
alphabet = list(OrderedDict.fromkeys(list(string)))
my_dict = {alphabet[i]: i+1 for i in range(len(alphabet))}

output = lzw(string)
print(my_dict)
print(output, ind, sep='\n')