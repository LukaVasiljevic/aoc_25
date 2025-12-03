joltage = 0

with open("in.txt") as f:
    for line in f.readlines():
        l = line.strip()
        nums = list(map(int, l))
        
        drop = len(l) - 12
        stack = []
        for d in l: 
            while drop > 0 and stack and stack[-1] < d: 
                stack.pop()
                drop -=1 
            stack.append(d)

        print(stack)
        result = stack[:12]

        joltage += int("".join(map(str, result)))

print(joltage)
