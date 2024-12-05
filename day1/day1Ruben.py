######################## 
###### PART 1 ##########
########################

right = []
left = []

with open("./day1/inputRuben.txt") as f:
    file = f.read().splitlines()

    for line in file:
        splitted_lines = line.split(" ")
        left.append(splitted_lines[0])
        right.append(splitted_lines[-1])

sortedRight = sorted(right)
sortedLeft = sorted(left)

ans1 = 0

for (left, right) in zip(sortedLeft, sortedRight):
    amount = abs(int(left) - int(right))
    ans1 += amount

print(ans1)


########################
###### PART 2 ##########
########################
from collections import Counter
setLeft = set(sortedLeft)
counterRight = Counter(sortedRight)
ans2 = 0

for left in setLeft:
    ans2 += int(left) * counterRight[left]

print(ans2)