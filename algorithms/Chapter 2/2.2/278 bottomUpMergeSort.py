def bottom_up_merge_sort(arr):
    k = 1
    while k <= len(arr):
        s = 0
        while s + k - 1 < len(arr):
            e = s + 2 * k - 1
            end = min(len(arr)-1, e)
            sort(arr, s, s+k-1, end)
            s += 2 * k
        k *= 2

def sort(arr, left, mid, right):
    if left >= right:
        return
    # merge in place
    cache = arr[left:right+1]
    lp = 0
    rp = mid + 1 - left
    for i in range(left, right+1):
        if lp > mid - left:
            arr[i] = cache[rp]
            rp += 1
        elif rp > right - left:
            arr[i] = cache[lp]
            lp += 1
        elif cache[lp] < cache[rp]:
            arr[i] = cache[lp]
            lp += 1
        else:
            arr[i] = cache[rp]
            rp += 1

arr = [4,25,7,4,1,0,3]
bottom_up_merge_sort(arr)
print(arr)