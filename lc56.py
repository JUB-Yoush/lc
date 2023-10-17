def merge(intervals):
    a = intervals[0]
    b = intervals[1]
    res = []
    for i in range(1,len(intervals)): 
        al = a[0]
        ar = a[1]
        bl = b[0]
        br = b[1]
        if bl <= ar:
            res.append([al,br])
            a = [al,br]
            if intervals[i+1] != None:
                b = intervals[i+1]
        else:
            res.append(b)
            a = b
            if intervals[i+1] != None:
                b = intervals[i+1]
    return res
            

print(merge([[1,3],[2,6],[8,10],[15,18]]))