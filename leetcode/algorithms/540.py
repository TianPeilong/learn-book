from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        n = len(nums)
        while left < right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid-1] == nums[mid]:
                if mid > 1 and (mid-1) % 2 == 1:
                    right = mid - 2
                else:
                    left = mid + 1
            elif mid < n-1 and nums[mid+1] == nums[mid]:
                if mid > 0 and mid % 2 == 1:
                    right = mid - 1
                else:
                    left = mid + 2
            else:
                return nums[mid]
        return nums[left]

nums = [1,1,2,3,3]
s = Solution()
print(s.singleNonDuplicate(nums))