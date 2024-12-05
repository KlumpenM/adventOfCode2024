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
safe = 0
ascending = True

with open("day2/inputRuben.txt", "r") as f:
    data = f.read().splitlines()
    # Iterating through the data
    for line in data:
        # Splitting the line into a list of integers
        levels = list(map(int, line.split()))
        # Enumerating each integer in the list
        for (i, _) in enumerate(levels):
            # If the integer is the last one in the list, break the loop
            if i == len(levels) - 1:
                safe += 1
                break
            # If the integer is the same as the next
            if levels[i] == levels[i + 1]:
                break
            # If the integer is smaller than the next
            if levels[i] < levels[i + 1]:
                if i == 0: 
                    ascending = True
                # If the difference between the integer and the next is greater than 3, break the loop
                if levels[i + 1] - levels[i] > 3 or not ascending:
                    break
                else:
                    continue
            
            # If the integer is greater than the next
            if levels[i] > levels[i + 1]:
                if i == 0:
                    ascending = False
                # If the difference between the integer and the next is greater than 3, break the loop
                if levels[i] - levels[i + 1] > 3 or ascending:
                    break
                else:
                    continue
print(safe)


########################
###### PART 2 ##########
########################

"""
Now we are allowed to remove 1 and only 1 level from the list.
So we are making a list safe
"""
safe = 0
ascending = True
amount_of_rules_removed = 0

# Found out that it's between 479 and 557

with open("day2/inputRuben.txt", "r") as f:
    data = f.read().splitlines()
    # Iterating through the data
    for line in data:
        # Splitting the line into a list of integers
        levels = list(map(int, line.split()))
        # Enumerating each integer in the list
        for (i, _) in enumerate(levels):
            # If the integer is the last one in the list, break the loop
            if i == len(levels) - 1:
                safe += 1
                break
                
            # If the integer is the same as the next, check two ahead
            if levels[i] == levels[i + 1]:
                if i + 2 < len(levels):
                    if levels[i] - levels[i + 2] > 3 or levels[i + 2] - levels[i] > 3:
                        break
                else:
                    safe += 1
                    break
            
            # If the integer is smaller than the next
            if levels[i] < levels[i + 1]:
                if i == 0: 
                    ascending = True
                # If the difference between the integer and the next is greater than 3, break the loop
                if levels[i + 1] - levels[i] > 3 or not ascending:
                    amount_of_rules_removed += 1
                    if amount_of_rules_removed > 1:
                        break
                    continue
                else:
                    continue

            # If the integer is greater than the next
            if levels[i] > levels[i + 1]:
                if i == 0:
                    ascending = False
                # If the difference between the integer and the next is greater than 3, break the loop
                if levels[i] - levels[i + 1] > 3 or ascending:
                    amount_of_rules_removed += 1
                    if amount_of_rules_removed > 1:
                        break
                    continue
                else:
                    continue
print(safe)