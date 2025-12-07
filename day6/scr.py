workbook = []
with open("in.txt") as f:
    for line in f.readlines():
        if line[0] in ["*", "+"]:
            workbook.append(line.split())
        else:
            workbook.append(list(map(int, line.split())))

print(workbook)

n = len(workbook)
m = len(workbook[0])
grand_total = 0
for j in range(m):
    operation = ""
    for i in range(n - 1, -1, -1):
        if not isinstance(workbook[i][j], int):
            operation = workbook[i][j]
            local_total = 1 if operation == "*" else 0
        else:
            if operation == "+":
                local_total += workbook[i][j]
            else:
                local_total *= workbook[i][j]
    grand_total += local_total

print(grand_total)
