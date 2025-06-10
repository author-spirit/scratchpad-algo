def check_available(intervals):
    
    intervals = sorted(intervals, key=lambda val: val[0])
    print(intervals)

    for i in range(len(intervals)-1):
        curr = intervals[i]
        next = intervals[i+1]
        if curr[-1] > next[0]:
            return False

    return True

intervals = [(9,15),(5,8)]
print(check_available(intervals))
