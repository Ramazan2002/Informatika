matrix = [[i * 5 + j + 1 for j in range(5)] for i in range(7)]
x = []
for i in range(len(matrix)):
    x += matrix[i]
#print(x)
y = [elem[:] for elem in matrix]
#print(y)
def sub(matrix, r1, r2, c1, c2):
    x = []
    for i in range(len(matrix)):
        y = []
        for j in range(len(matrix[i])):
            y.append(matrix[r1:r2+1])
        x.append(y)
    return x
print(sub(matrix, 1, 3, 3, 5))