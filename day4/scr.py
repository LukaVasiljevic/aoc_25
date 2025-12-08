def canAccess(prev, curr, next, i, j):
    adjecent = 0
    if prev != []:
        if j - 1 >= 0:
            if prev[j - 1] == "@":
                adjecent += 1
        if j + 1 < len(prev):
            if prev[j + 1] == "@":
                adjecent += 1
        if prev[j] == "@":
            adjecent += 1

    if j - 1 >= 0:
        if curr[j - 1] == "@":
            adjecent += 1
    if j + 1 < len(curr):
        if curr[j + 1] == "@":
            adjecent += 1

    if next != []:
        if j - 1 >= 0:
            if next[j - 1] == "@":
                adjecent += 1
        if j + 1 < len(next):
            if next[j + 1] == "@":
                adjecent += 1
        if next[j] == "@":
            adjecent += 1

    return 1 if adjecent < 4 else 0


maze = []
with open("in.txt") as f:
    for line in f.readlines():
        maze += [list(line.strip())]

n = len(maze)
m = len(maze[0])

accesible_rolls = 0

for i in range(0, n):
    prev_row = maze[i - 1] if i - 1 >= 0 else []
    next_row = maze[i + 1] if i + 1 < m else []
    for j in range(0, m):
        if maze[i][j] == "@":
            accesible_rolls += canAccess(prev_row, maze[i], next_row, i, j)

print(accesible_rolls)
