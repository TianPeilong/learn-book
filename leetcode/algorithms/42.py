class Solution:
    def trap(self, height):
        if len(height) < 3:
            return 0
        mid = height.index(max(height))
        left = None
        right = None
        if mid == 0:
            left = []
            right = height[::-1]
        elif mid == len(height)-1:
            left = height
            right = []
        else:
            left = height[:mid+1]
            right = height[len(height)-1:mid-1:-1]
        return self.left_to_right(left) + self.left_to_right(right)

    def left_to_right(self, height):
        if len(height) < 3:
            return 0
        total = 0
        left = 0
        while height[left] == 0:
            left += 1
        while left < len(height):
            right = left + 1
            while right < len(height):
                if height[left] <= height[right]:
                    for i in range(left + 1, right):
                        total += height[left] - height[i]
                    break
                right += 1
            left = right
        return total

height = [0,1,0,4,1,0,1,4,2,1,2,1]
t = Solution()
print(t.trap(height))