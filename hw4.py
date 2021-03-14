from random import randint

def generate(n, m, random = False):
    if random:
        return [[randint(1, 15) for j in range(m)] for i in range(n)]
    else:
        return [[0] * m for i in range(n)]

x = generate(5, 5, True)

def simple(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 1
            elif i < j:
                matrix[i][j] = 2
            else:
                matrix[i][j] = 0
    return matrix


def maximal(matrix, row = False, col = False):
    maxx = -1
    if row:
        k = -1
        for line in matrix:
            s = sum(line)
            k += 1
            if s > maxx:
                maxx = s
                no = k
        return matrix[no]
    
    if col:
        k = 0
        for col in zip(*matrix):
            s = 0
            for i in col:
                s += i
            k += 1
            if s > maxx:
                maxx = s
                no = k
        return [x[no - 1] for x in matrix]


def sub(matrix, r1, r2, c1, c2):
    x = matrix[r1:r2+1][:]
    for i in range(len(x)):
        x[i] = x[i][c1:c2+1]

    return x

def rotate(matrix, r1, r2, c1, c2):
    if (r2 - r1) == (c2 - c1):
        x = sub(matrix, r1, r2, c1, c2)
        y = []
        for i in range(len(x)):
            z = []
            for j in range(len(x[i])):
                z.append(x[j][i])
            y.append(z)
        k = 0
        for i in range(r1, r2 + 1):
            l = 0
            for j in range(c1, c2 + 1):
                matrix[i][j] = y[k][l]
                l += 1
            k += 1
        return matrix
