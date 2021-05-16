from matplotlib import pyplot as plt
from math import hypot
from functools import partial
from time import time
from multiprocessing import Pool#

def distance(x1, y1, x2, y2):
    return hypot(x2 - x1, y2 - y1)

def find(database):
    b = {}
    a = list(database.values())
    for i in range(len(a) - 1):
        k = 0
        for j in range(1, len(a)):
            if (i != j) and (distance(a[i][0], a[i][1], a[j][0], a[j][1]) <= 0.5):
                k += 1
                b[list(database.keys())[i]] = k
    return b

def for_task2(lst, value):
    flag = True
    for elem in lst:
        if distance(elem[0], elem[1], value[0], value[1]) < 1:
            flag = False
    return flag

def area(a):
    return 0.7 * a / 18

def read_data(path):
    with open(path, 'r', encoding = 'utf8') as file:
        d = []
        c = {}
        for line in file:
            d.append(line.strip().split('\t'))
        for elem in d:
            a, *b = elem
            c[a] = tuple(map(float, b))
    return c

def task1(database, c):
    for key in c:
        maxx = max(list(c.values()))
        if maxx == c[key]:
            return (database[key][0], database[key][1])

def task2(database):
    maxx = 0
    k = 0
    top_10 = []
    empty = 0
    for i in range(10):
        for elem in database:
            if for_task2(top_10, database[elem]):
                for good in database:
                    if distance(database[elem][0], database[elem][1],
                                database[good][0], database[good][1]) <= 0.5:
                        maxx += 1
                if maxx > k:
                    k = maxx
                    empty = (database[elem][0], database[elem][1])
                maxx = 0
        k = 0
        top_10.append(empty)
    return top_10

def task3(database):
    top_15 = []
    k = 0
    empty = 0
    humans = 0
    for i in range(15):
        for house in database:
            if for_task2(top_15, database[house]):
                for ned_house in database:
                    if distance(database[house][0], database[house][1],
                                database[ned_house][0], database[ned_house][1]) <= 0.5:
                        humans += area(database[ned_house][2])
                if humans > k:
                    k = humans
                    empty = (database[house][0], database[house][1])
                humans = 0
        k = 0
        top_15.append(empty)
    return top_15

def plot(database, best_coords):
    """
    НЕ МЕНЯТЬ КОД!
    Отрисовка точек 2D
    Args:
        database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
        best_coords (list): для задачи 1 это (x, y), для задачи 2-3 это [(x1,y1), (x2,y2) ... (xn,yn)]
    """
    plt.close()
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.plot([coord[0] for coord in database.values()],
             [coord[1] for coord in database.values()], '.', ms=5, color='k', alpha=0.5)
    if isinstance(best_coords[0], tuple):
        for x, y in best_coords:
            circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
            ax.add_patch(circle)
        plt.plot([coord[0] for coord in best_coords],
                 [coord[1] for coord in best_coords], '.', ms=15, color='r')
    elif isinstance(best_coords[0], float):
        x, y = best_coords
        circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
        ax.add_patch(circle)
        plt.plot(*best_coords, '.', ms=15, color='r')
    else:
        raise ValueError("Проверь, что подаёшь список кортежей или кортеж из двух координат")
    plt.show()

if __name__ == '__main__':
    path = r"/IT/Infa/buildings.txt"
    x = time()
    pool1 = Pool(1)
    pool2 = Pool(1)
    database = read_data(path)
    c = pool2.apply_async(find, (database,)).get()
    ko = partial(task1, database)
    best_task1 = pool1.apply_async(ko, (c,)).get()
    best_task2 = pool2.apply_async(task2, (database,)).get()
    best_task3 = pool1.apply_async(task3, (database,)).get()
    y = time()
    plot(database, best_task1)
    plot(database, best_task2)
    plot(database, best_task3)
    pool1.close()
    pool2.close()
    pool1.join()
    pool2.join()
    with open('different.txt', 'w+', encoding='utf-8') as f:
        print('New', y - x, file=f)
