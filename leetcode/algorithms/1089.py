class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_stack = []
        n = len(arr)
        for i,v in enumerate(arr):
            if v == 0:
                zero_stack.append(i)
        if not zero_stack:
            return
        while zero_stack:
            if zero_stack[-1] + len(zero_stack) - 1 >= n:
                zero_stack.pop()
            else:
                break
        old_pos = zero_stack.pop()
        new_pos = len(zero_stack) + old_pos
        if new_pos + 2 < n:
            arr[new_pos+2:] = arr[old_pos+1:old_pos+1+n-new_pos-2]
        if new_pos + 1 < n:
            arr[new_pos+1] = 0
        arr[new_pos] = 0
        last = new_pos
        while zero_stack:
            old_pos = zero_stack.pop()
            new_pos = len(zero_stack) + old_pos
            if new_pos + 2 != last:
                arr[new_pos+2:last] = arr[old_pos+1:old_pos+1+last-new_pos-2]
            arr[new_pos+1] = 0
            arr[new_pos] = 0
            last = new_pos

s = Solution()
arr = [1,0,0,2,3,0,4,5,0]
s.duplicateZeros(arr)
print(arr)