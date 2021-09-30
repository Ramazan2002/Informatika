from random import randint
a = [[randint(0,255) for i in range(5)] for j in range(5)]
b = [[0.0 for k in range(5)] for v in range(5)]

for line in a:
    print(line)

for i in range(len(a)):
    sum = 0
    for j in range(len(a[i])):
        if i == 0:
            if j == 0:
                sum = (a[i][j] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]) / 4
            elif j == (len(a[i]) - 1):
                sum = (a[i][j] + a[i][j - 1] + a[i + 1][j - 1] + a[i + 1][j]) / 4
            else:
                sum = (a[i][j - 1] + a[i][j] + a[i][j + 1] + a[i + 1][j + 1] + a[i + 1][j] + a[i + 1][j - 1]) / 6
        elif i == (len(a) - 1):
            if j == len(a[i]) - 1:
                sum = (a[i][j] + a[i - 1][j - 1] + a[i - 1][j] + a[i][j - 1]) / 4
            elif j == 0:
                sum = (a[i][j] + a[i - 1][j] + a[i - 1][j + 1] + a[i][j + 1]) / 4
            else:
                sum = (a[i][j] + a[i - 1][j - 1] + a[i - 1][j] + a[i - 1][j + 1] + a[i][j + 1] + a[i][j - 1]) / 6
        elif j == 0:
            if i == 0:
                sum = (a[i][j] + a[i][j + 1] + a[i + 1][j] + a[i + 1][j + 1]) / 4
            elif i == (len(a) - 1):
                sum = (a[i][j] + a[i - 1][j] + a[i - 1][j + 1] + a[i][j + 1]) / 4
            else:
                sum = (a[i][j] + a[i-1][j] + a[i-1][j+1] + a[i][j+1] + a[i+1][j] + a[i+1][j+1]) / 6
        elif j == (len(a[i]) - 1):
            if i == 0:
                sum = (a[i][j] + a[i][j-1] + a[i+1][j-1] + a[i+1][j]) / 4
            elif i == (len(a) - 1):
                sum = (a[i][j] + a[i - 1][j - 1] + a[i - 1][j] + a[i][j - 1]) / 4
            else:
                sum = (a[i][j] + a[i - 1][j - 1] + a[i - 1][j] + a[i][j-1] + a[i+1][j-1] + a[i+1][j]) / 6
        else:
            sum = (a[i-1][j-1] + a[i-1][j] + a[i-1][j+1] + a[i][j-1]+a[i][j]+
                   a[i][j+1] + a[i+1][j-1] + a[i+1][j] + a[i+1][j+1]) / 9
        b[i][j] = sum
print()
for line in b:
    print(line)
