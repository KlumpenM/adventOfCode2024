import re

ans = 0
with open('day3/inputRuben.txt') as f:
    data = f.read().strip()
    results = re.findall("mul\([0-9]+,[0-9]+\)", data)
    for mul in results:
        left, right = mul[4:-1].split(",")
        ans += int(left) * int(right)

print(ans)



#################
#### PART 2 #####
#################
ans = 0
do = True

with open('day3/inputRuben.txt') as f:
    data = f.read().strip()
    results = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)", data)
    for mul in results:
        if mul == "don't()":
            do = False
        elif mul == "do()":
            do = True
        if do and mul.startswith("mul"):
            left, right = mul[4:-1].split(",")
            ans += int(left) * int(right)

print(ans)


