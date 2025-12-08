diagram = []
with open('in.txt') as f:
    for line in f.readlines():
        diagram += [list(line.strip())]

beams = {70}
splitted = 0

for row in diagram[1:]:
    temp = []
    for beam in beams:
        if row[beam] == '^':
            splitted += 1
            temp += [beam - 1, beam + 1]
        else:
            temp.append(beam)
    beams = set(temp) 
    
print(splitted)
