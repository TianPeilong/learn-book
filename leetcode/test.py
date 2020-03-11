class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        status = [0] * len(light)
        count = 0
        cur = 0
        c = 0
        j = 0
        i = 0
        t = 0
        maxL = 0
        while i < len(light):
            curMax = light[i] if light[i] > maxL else maxL
            if curMax == i + 1:
                count += 1
                t = curMax
                i += 1
            else:
                start = j if i < j else j
                for j in range(start, light[j]):
                    if light[j] > maxL:
                        t = j
                        maxL = light[j]
                i = light[i] - 1
        return count
    


case=[2,1,3,5,4]
t = Solution()
print(t.numTimesAllBlue(case))
input()