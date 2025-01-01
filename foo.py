def sort(A,lower,upper):

    buckets = [0] * (upper - lower +1)
    for num in A:
        pos = num - lower
        buckets[pos] += 1
    A = []
    for i in range(len(buckets)):
        for j in range(buckets[i]):
            A.append(i + lower)
    return A

b = [3,8,1,5,9,2,3,2,4,1,5,6]
print(b)
print(sort(b,1,9))
