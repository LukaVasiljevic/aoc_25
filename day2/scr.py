import re 
pattern = r"(.+?)(?=\1+$|$)"


ranges = []
with open('in.txt') as f:
    for a in f.read().split(','):
        ranges.append(list(a.split('-')))


s = 0

for r in ranges:
    for i in range(int(r[0]), int(r[1]) + 1):     
        matches = re.findall(pattern,str(i))
        if len(matches) == 2 or (len(matches) % 2 == 0 and len(set(matches)) == 1):
            s += int("".join(matches))
print(s)