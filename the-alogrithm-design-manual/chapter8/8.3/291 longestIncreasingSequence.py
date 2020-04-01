def longestIncreasingSequence(arr):
    if not arr:
        return []
    if len(arr) == 1:
        return arr
    n = len(arr)
    aux = [None] * n
    lens = [0] * n
    lens[0] = 1
    maxl = (0, 1)
    for i in range(1,n):
        pre = None
        j = i - 1
        while j >= 0:
            if arr[j] < arr[i] and (pre is None or lens[j] > lens[pre]):
                pre = j
            j -= 1
        if pre is None:
            lens[i] = 1
        else:
            lens[i] = lens[pre] + 1
            aux[i] = pre
        if lens[i] > maxl[1]:
            maxl = (i, lens[i])
    result = []
    p = maxl[0]
    while p is not None:
        result.append(arr[p])
        p = aux[p]
    return [num for num in reversed(result)]

ar = [2, 4, 3, 5, 1, 7, 6, 9, 8]
print(longestIncreasingSequence(ar))