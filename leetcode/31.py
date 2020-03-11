class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                cur = i - 1
                j = i
                while j < n:
                    if nums[j] <= nums[cur]:
                        break
                    j += 1
                self.switch(nums, cur, j-1)
                for x in range(i, i + (n - i) // 2):
                    self.switch(nums, x, n - x + cur)
                break
            i -= 1
        if i == 0:
            for x in range(n // 2):
                self.switch(nums, x, n - x - 1)
    
    def switch(self, nums, i, j):
        c = nums[i]
        nums[i] = nums[j]
        nums[j] = c


nums = [1,3,2]
t = Solution()
print(t.nextPermutation(nums))
input()