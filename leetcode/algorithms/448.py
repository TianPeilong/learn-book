from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] <= 0:
                i += 1
            else:
                p = nums[i] - 1
                if p == i:
                    nums[i] = 0
                elif nums[p] == 0:
                    nums[i] = -1
                elif nums[p] == -1:
                    nums[p] = 0
                    nums[i] = -1
                else:
                    nums[i] = nums[p]
                    nums[p] = 0
        unexist = []
        for i,c in enumerate(nums):
            if c == -1:
                unexist.append(i+1)
        return unexist

nums = [4,3,2,7,8,2,3,1]
s = Solution()
print(s.findDisappearedNumbers(nums))