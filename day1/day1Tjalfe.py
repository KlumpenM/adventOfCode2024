from collections import Counter

right = []
left = []

ans = 0

with open("./day1/inputTjalfe.txt") as f:
    file = f.read().splitlines()
    for line in file:
        curLeft, curRight = line.split("   ")
        left.append(int(curLeft))
        right.append(int(curRight))
    left.sort()
    right.sort()
    ans = sum(abs(l-r) for l, r in zip(left, right))


    # Part 2
    ans = 0
    left = set(left)
    right = Counter(right)
    for l in left:
        ans += l * right[l]
    print(ans)