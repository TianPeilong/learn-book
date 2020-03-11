class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if nums[0] > nums[-1]:
            return self.searchIn(nums, target, 0, len(nums) - 1)
        else:
            return self.searchNormal(nums, target, 0, len(nums) - 1)
        
    def searchIn(self, nums, target,  i, j):
        if nums[i] < nums[j]:
            return self.searchNormal(nums, target, i, j)
        if i > j:
            return -1
        if i == j:
            return i if nums[i] == target else -1
        m = (i + j) // 2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            if nums[i] <= nums[m] and nums[i] > target:
                return self.searchIn(nums, target, m+1, j)
            else:
                return self.searchIn(nums, target, i, m-1)
        else:
            if nums[j] < target and nums[j] >= nums[m]:
                return self.searchIn(nums, target, i, m-1)
            else:
                return self.searchIn(nums, target, m+1, j)

    def searchNormal(self, nums, target, i, j):
        if i == j:
            return i if nums[i] == target else -1
        m = (i + j) // 2
        if nums[m] >= target:
            return self.searchNormal(nums, target, i, m)
        else:
            return self.searchNormal(nums, target, m + 1, j)

nums = [3,1]
target = 3
t = Solution()
print(t.search(nums, target))
input()