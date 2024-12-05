
safe = 0
ascending = True

with open("./day2/inputTjalfe.txt") as f:
    file = f.read().splitlines()

    for line in file:
        levels = list(map(int, line.split()))
        for i in range(len(levels)):
            if (i == len(levels)-1):
                safe += 1
                break
            if (levels[i] == levels[i+1]):
                break
            if (levels[i] < levels[i+1]):
                if (i == 0):
                    ascending = True
                if ((levels[i+1] - levels[i]) > 3 or not ascending):
                    break
                else:
                    continue
            if (levels[i] > levels[i+1]):
                if (i == 0):
                    ascending = False
                if ((levels[i] - levels[i+1]) > 3 or ascending):
                    break
                else:
                    continue
    print(safe)
            
