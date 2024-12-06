import re

ans = 0
do = True
with open("./day3/inputTjalfe.txt") as f:
    file = f.read().strip()
    result = re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", file)
    for elem in result:
        if (elem == "do()"):
            do = True
        if (elem == "don\'t()"):
            do = False
        if (elem[0:2] == "mul" and do):
            left, right = elem[4:-1].split(",")
            ans += int(left) * int(right)
    print(ans)