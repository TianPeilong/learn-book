class Solution:
    def sumFourDivisors(self, nums):
        oset = set()
        count = 0
        for n in nums:
            count += self.getCount(n,oset)
        return count
    
    def getCount(self, num, oset):
        if num in oset:
            return 0
        count = 0
        ins = set()
        for i in range(1, num//2 + 1):
            if num % i == 0:
                ins.add(i)
                ins.add(num//i)
                if len(ins) > 4:
                    break
            if i ** 2 > num:
                break
        if len(ins) == 4:
            count = sum(ins)
        if len(ins) > 4:
            oset.add(num)
        return count
        
        
s = Solution()
print(s.sumFourDivisors([7286,18704,70773,8224,91675]))