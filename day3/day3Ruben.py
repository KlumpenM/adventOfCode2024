import re

ans = 0
with open('day3/inputRuben.txt') as f:
    data = f.read().strip()
    results = re.findall("mul\([0-9]+,[0-9]+\)", data)
    for mul in results:
        left, right = mul[4:-1].split(",")
        ans += int(left) * int(right)

print(ans)