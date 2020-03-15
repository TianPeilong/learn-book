class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        r = 0
        w = 0
        b = len(nums) - 1
        while w <= b:
            cur = nums[w]
            if cur == 0:
                if w != r:
                    self.switch(nums, w, r)
                r += 1
                w += 1
            elif cur == 2:
                if w == b:
                    break
                else:
                    self.switch(nums, w, b)
                    b -= 1
            else:
                w += 1
        return nums

    def switch(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


case = [1,2,0]
t = Solution()
print(t.sortColors(case))