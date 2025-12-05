with open('in.txt') as f:
    ranges, _ = f.read().split('\n\n')

    intervals = []
    for r in ranges.split():
        intervals.append(list(map(int, r.split(('-')))))
    
    intervals.sort()
    merged = []
    n  = len(intervals)
    merged.append(intervals[0])
    for i in range(1, n):
        last = merged[-1]
        curr = intervals[i]
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            merged.append(curr)
    
    
    fresh = sum(e - s + 1 for s, e in merged)
    print(fresh)