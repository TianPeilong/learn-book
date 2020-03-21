def bubble_sort(arr):
    n = len(arr) - 1
    while n > 1:
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        n -= 1

arr = [3,4,62,1,3,5,3]
bubble_sort(arr)
print(arr)