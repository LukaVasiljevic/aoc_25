joltage = 0

with open("in.txt") as f:
    for line in f.readlines():
        l = line.strip()
        nums = list(map(int, l))
        
        best = -1

        n = len(l)
        for i in range(n):
            for j in range(i+1, n):
                val = int(f"{nums[i]}{nums[j]}")
                if val > best:
                    best = val
        joltage += best

print(joltage)