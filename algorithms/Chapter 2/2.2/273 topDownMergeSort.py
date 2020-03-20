# merge in place
def top_down_merge_sort(arr):
    if not arr:
        return
    sort(arr, 0, len(arr)-1)
    
def sort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    sort(arr, left, mid)
    sort(arr, mid+1, right)
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
top_down_merge_sort(arr)
print(arr)