def canAccess(prev, curr, next, i, j):
    adjecent = 0
    neigh = []
    if prev != []:
        if j - 1 >= 0:
            if prev[j - 1] == "@":
                neigh.append((i - 1, j - 1))
                adjecent += 1
        if j + 1 < len(prev):
            if prev[j + 1] == "@":
                neigh.append((i - 1, j + 1))
                adjecent += 1
        if prev[j] == "@":
            neigh.append((i - 1, j))
            adjecent += 1

    if j - 1 >= 0:
        if curr[j - 1] == "@":
            neigh.append((i, j - 1))
            adjecent += 1
    if j + 1 < len(curr):
        if curr[j + 1] == "@":
            neigh.append((i, j + 1))
            adjecent += 1

    if next != []:
        if j - 1 >= 0:
            if next[j - 1] == "@":
                adjecent += 1
                neigh.append((i + 1, j - 1))
        if j + 1 < len(next):
            if next[j + 1] == "@":
                adjecent += 1
                neigh.append((i + 1, j + 1))
        if next[j] == "@":
            neigh.append((i + 1, j))
            adjecent += 1

    return 1 if adjecent < 4 else 0


maze = []
with open("in.txt") as f:
    for line in f.readlines():
        maze += [list(line.strip())]

n = len(maze)
m = len(maze[0])

cond = True
moved_rolls = 0
while cond:
    accesible_rolls = []
    for i in range(0, n):
        prev_row = maze[i - 1] if i - 1 >= 0 else []
        next_row = maze[i + 1] if i + 1 < m else []
        for j in range(0, m):
            if maze[i][j] == "@":
                if canAccess(prev_row, maze[i], next_row, i, j) == 1:
                    accesible_rolls.append((i, j))
    for k, l in accesible_rolls:
        maze[k][l] = "."
    moved_rolls += len(accesible_rolls)
    if accesible_rolls == []:
        cond = False

print(moved_rolls)
