def exchange(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def shell_sort(arr):
    k = 1
    n = len(arr)
    while k < n/3:
        k = 3 * k + 1
    while k >= 1:
        for i in range(k, n):
            j = i
            while j >= k:
                if arr[j] < arr[j-1]:
                    exchange(arr, j-1, j)
                j -= k
        k = k // 3

arr = [4,25,7,4,1,0,3]
shell_sort(arr)
print(arr)