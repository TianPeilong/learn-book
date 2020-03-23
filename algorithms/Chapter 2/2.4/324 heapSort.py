def sink(arr, k, n):
    while 2*k <= n:
        j = 2*k
        if j < n and arr[j+1]>arr[j]:
            j += 1
        if arr[k] < arr[j]:
            arr[k],arr[j] = arr[j],arr[k]
        else:
            break

def heap_sort(arr):
    n = len(arr)-1
    mid = n // 2
    for i in range(mid, 0, -1):
        sink(arr, i, n)
    j = 1
    while n > 1:
        arr[1],arr[n] = arr[n],arr[1]
        n -= 1
        sink(arr, 1, n)

arr = [0,1,2,9,3,0,2,5]
heap_sort(arr)
print(arr)