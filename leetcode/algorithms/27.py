class Solution:
    def removeElement(self, nums, val):
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        while nums[right] == val and right >= 0:
            right -= 1
        while left <= right:
            if nums[right] == val:
                right -= 1
                continue
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
                left += 1
            else:
                left += 1
        return right + 1

case = [0,1,2,2,3,0,4,2]
t = Solution()
print(t.removeElement(case, 2))
input()