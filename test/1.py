from typing import List
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        if len(stoneValue) == 1:
            return stoneValue[0] > 0
        av = 0
        bv = 0
        n = len(stoneValue)
        i = 0
        while i < len(stoneValue):
            maxd = None
            if i == len(stoneValue) - 1:
                av += stoneValue[i]
                i += 1
                continue
            ia = i
            fbe,fmb = self.get(i+1, min(i+3,n-1), stoneValue)
            maxd = (stoneValue[i]-fmb, i, i+1, fbe)
            while ia < min(i + 3, n):
                suma = sum(stoneValue[i:ia+1])
                ib = ia + 1
                if ib >= n:
                    d = suma
                    if suma > maxd[0]:
                        maxd = (suma, i, ib, ib)
                    break
                else:
                    be,mb = self.get(ib, min(ib+2,n-1), stoneValue)
                    if suma - mb > maxd[0]:
                        maxd = (suma-mb, i, ib, be)
                ia += 1
            av += maxd[0]
            i = maxd[3] + 1
        if av == bv:
            return 'Tie'
        else:
            return 'Alice' if av > bv else 'Bob'
                
    def get(self, s, e, stoneValue):
        if s == e:
            return (s, stoneValue[s])
        curi = s
        curV = stoneValue[s]
        t = curV
        for i in range(s+1, e+1):
            t += stoneValue[i]
            if t > curV:
                curi = i
                curV = t
        return (curi, curV)
t = Solution()
print(t.stoneGameIII([-1,-2,-3]))