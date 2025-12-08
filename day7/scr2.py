diagram = []
with open("in.txt") as f:
    for line in f.readlines():
        diagram += [list(line.strip())]

beams = {70: 1}

for row in diagram[1:]:
    temp = {}

    for i, count in beams.items():
        if row[i] == "^":
            temp[i - 1] = temp.get(i - 1, 0) + count
            temp[i + 1] = temp.get(i + 1, 0) + count
        else:
            temp[i] = temp.get(i, 0) + count
    beams = temp

print(sum(beams.values()))
