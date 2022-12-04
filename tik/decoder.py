code = float(input())
length = int(input())
alphabet = input()
p = list(map(eval, input().split()))


word = ''
left, right = 0, 1

for _ in range(length):
    for i, letter in enumerate(alphabet):
        interval = (left + (right - left) * sum(p[:i]),
                    left + (right - left) * sum(p[:i + 1]))

        if interval[0] <= code < interval[1]:
            word += letter
            code = (code - interval[0]) / (interval[1] - interval[0])
            break

print(word)
