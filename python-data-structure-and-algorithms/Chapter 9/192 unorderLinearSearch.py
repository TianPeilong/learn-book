def search(arr, item):
    for i,cur in enumerate(arr):
        if cur == item:
            return i
    return None