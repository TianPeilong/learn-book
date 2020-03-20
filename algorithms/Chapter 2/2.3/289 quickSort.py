def exchange(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partion(arr, left, right):
    if left >= right:
        return
    lo = left
    lp = lo + 1
    rp = right
    while True:
        while lp < right and arr[lo] >= arr[lp]:
            lp += 1
        while rp > left and arr[lo] <= arr[rp]:
            rp -= 1
        if lp >= rp:
            break
        exchange(arr, lp, rp)
    exchange(arr, lo, rp)
    partion(arr, left, rp - 1)
    partion(arr, rp + 1, right)

def quick_sort(arr):
    partion(arr, 0, len(arr)-1)

arr = [4,25,7,4,1,0,3,3]
quick_sort(arr)
print(arr)