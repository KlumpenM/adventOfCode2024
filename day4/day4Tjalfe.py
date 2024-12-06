
suffix = 'MAS'
ans = 0
with open("./day4/inputTjalfe.txt") as f:
    file = f.read().strip()

# Two dimensional array setup.
arr = [list(line) for line in file.split("\n")]
n,m = len(arr), len(arr[0])

for i in range(n):
    for j in range(m):
        currentElem = arr[i][j]
        if (currentElem != 'X'):
            continue
        # To the right
        if (j < m-3):
            if (str(arr[i][j+1] + arr[i][j+2] + arr[i][j+3]) == suffix):
                ans += 1
        # To the left
        if (j > 2):
            if (str(arr[i][ j-1] + arr[i][ j-2] + arr[i][ j-3]) == suffix):
                ans += 1
        # Downward
        if (i < n-3):
            if (str(arr[i+1][j] + arr[i+2][j] + arr[i+3][j]) == suffix):
                ans += 1
        # Upwards
        if (i > 2):
            if (str(arr[i-1][j] + arr[i-2][j] + arr[i-3][j]) == suffix):
                ans += 1
        # Left-Down diagonal
        if (j > 2 and i < n-3):
            if (str(arr[i+1][j-1] + arr[i+2][j-2] + arr[i+3][j-3]) == suffix):
                ans += 1
        # Left-Up diagonal
        if (j > 2 and i > 2):
            if (str(arr[i-1][j-1] + arr[i-2][j-2] + arr[i-3][j-3]) == suffix):
                ans += 1
        # Right-Down diagonal
        if (j < m-3 and i < n-3):
            if (str(arr[i+1][j+1] + arr[i+2][j+2] + arr[i+3][j+3]) == suffix):
                ans += 1
        # Right-Up diagonal
        if (j < m-3 and i > 2):
            if (str(arr[i-1][j+1] + arr[i-2][j+2] + arr[i-3][j+3]) == suffix):
                ans += 1
print(ans)