safe = 0
with open("./day2/inputTjalfeTest.txt") as f:
    file = f.read().splitlines()

    for line in file:
        levels = list(map(int, line.split()))
        ascending = True
        unsafe = False
        secondUnsafety = False
        removedElements = 0
        for i in range(len(line)):
            if (i > 1 and removedElements > 0):
                i = i-removedElements-1
            else:
                i = i-removedElements
            if unsafe:
                if secondUnsafety:
                    break
                unsafe = False
                secondUnsafety = True
            if (i == len(levels)-1 or i == len(levels)):
                print(line)
                safe += 1
                break
            if (levels[i] == levels[i+1]):
                unsafe = True
                levels.pop(i)
                removedElements += 1
                continue
            if (levels[i] < levels[i+1]):
                if (i == 0):
                    ascending = True
                if ((levels[i+1] - levels[i]) > 3 or not ascending):
                    unsafe = True
                    if(not ascending):
                        levels.pop(i)
                        removedElements += 1
                    else:
                        levels.pop(i+1)
                        removedElements += 1
                    continue
            if (levels[i] > levels[i+1]):
                if (i == 0):
                    ascending = False
                if ((levels[i] - levels[i+1]) > 3 or ascending):
                    unsafe = True
                    if(ascending):
                        levels.pop(i)
                        removedElements += 1
                    else:
                        levels.pop(i+1)
                        removedElements += 1
                    continue
    print(safe)
            
