def interpolation_search(orderd_list, term):
    left = 0
    right = len(orderd_list) - 1
    while left <= right:
        mid = left + ((right - left) * (term - orderd_list[left])) // (orderd_list[right] - orderd_list[left])
        if mid > right or mid < left:
            return None
        if orderd_list[mid] == term:
            return mid
        elif orderd_list[mid] < term:
            left = mid + 1
        else:
            right = mid - 1
    return None