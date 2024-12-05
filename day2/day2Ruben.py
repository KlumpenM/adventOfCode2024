########################
###### PART 1 ##########
########################

"""
Description:
The unusual data (your puzzle input) consists of many reports, one report per line. 
Each report is a list of numbers called levels that are separated by spaces. 
    For example:
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9

So, a report only counts as safe if both of the following are true:
- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.          
"""
unsafe = 0
safe = 0

with open("day2/inputRuben.txt", "r") as f:
    data = f.read().splitlines()
    print(len(data))

    # Iterating through the data
    for line in data:
        # Splitting the line into a list of integers
        levels = list(map(int, line.split()))
        for i in range(len(levels)-1):
            # If the difference between two adjacent levels is greater than 3
            if abs(levels[i] - levels[i+1]) > 3:
                unsafe += 1
                break

print(1000 - unsafe)
