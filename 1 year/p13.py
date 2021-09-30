from random import choice
import pickle
with open('1.csv', 'r', encoding='utf-8') as f:
    file = f.readlines()
    words = {}
    for line in file:
        line = line.split()
        if line[1] == 's':
            words[line[0]] = line[2]
    sort = sorted(words.items(), key=lambda x: x[1], reverse=True)
    sort = list(filter(lambda x: (float(x[1]) > 4) and (float(x[1]) < 10), sort))
    for i in range(len(sort)):
        sort[i] = sort[i][0]
    print(sort)
    pickle.dump(sort, open('123456.pickle', 'wb'))

with open('123456.pickle', 'rb') as f:
    data = pickle.load(f)
    flag = True
    word = choice(data)
    y = word
    k = 10
    while flag:
        x = input('Введите букву ')
        if x in y:
            y = y.replace(x, '', 1)
            print('Правильно')
        else:
            k -= 1
            if k < 1:
                flag = False
            print('Осталось попыток', k)
    print(word)