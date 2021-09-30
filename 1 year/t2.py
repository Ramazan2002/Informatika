def best_of_the_best(a):
    return (y:=max(x:={k: a.count(k) for k in a}, key=x.get), a.count(y))

print(best_of_the_best(['PHP', 'PHP', 'Python', 'PHP',
                        'Python', 'JS', 'Python',
                        'Python', 'PHP', 'Python']))

def do_you_know_da_way(a, words):
    c = iter(a) # Можно было без итератора, но мне так захотелось :3
    b = ''
    h = []
    for i in range(len(a)):
        if (x:=next(c)) in words:
            b += x
        else:
            h.append(b)
            b=''
    return max(h, key=lambda x: len(x))


print(do_you_know_da_way('acbfbacffaabbccufacbbafaa', ['a', 'b', 'c']))

def priffki(s):
    o = ''
    for a in s:
        if a.islower():
            o += a.upper()
        else:
            o += a.lower()
    return o

print(priffki('Привет, Oleg! Это FBI!'))

def big_smoke(a):
    b = a.split(' ')
    u = b[:]
    c = max(b, key=lambda x: len(x))
    n1 = b.index(c)
    b.pop(n1)
    d = max(b, key=lambda x: len(x))
    n2 = b.index(d)
    return ' '.join(u[n1:n2+2])

print(big_smoke("I'll have two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a laaarge soda"))