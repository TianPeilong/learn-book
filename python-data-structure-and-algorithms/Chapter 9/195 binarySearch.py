def binary_search(orderd_list, term):
    left = 0
    right = len(orderd_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if orderd_list[mid] == term:
            return mid
        elif orderd_list[mid] < term:
            left = mid + 1
        else:
            right = mid - 1
    return None

def binary_search_recursive(orderd_list, term):
    return _binary_search_recursive(orderd_list, 0, len(orderd_list)-1, term)

def _binary_search_recursive(orderd_list, left, right, term):
    if left > right:
        return None
    mid = (left + right) // 2
    if orderd_list[mid] == term:
        return mid
    elif orderd_list[mid] < term:
        return _binary_search_recursive(orderd_list, mid + 1, right, term)
    else:
        return _binary_search_recursive(orderd_list, left, mid - 1, term)

l = [0,5,6,7,8,9,34]
print(binary_search(l, 8))
print(binary_search_recursive(l, 8))
