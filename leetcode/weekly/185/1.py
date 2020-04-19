from typing import List

class Solution:
    def reformat(self, s: str) -> str:
        if len(s) < 2:
            return s
        ns = []
        cs = []
        n0 = ord('0')
        n9 = ord('9')
        for c in s:
            if ord(c) >= n0 and ord(c) <= n9:
                ns.append(c)
            else:
                cs.append(c)
        re = ''
        if len(ns) < len(cs):
            ns, cs = cs, ns
        if len(ns) - len(cs) >= 2:
            return ''
        pn = 0
        ps = 0
        isN = False
        while pn < len(ns) and ps < len(cs):
            if isN:
                re += cs[ps]
                ps += 1  
            else:
                re += ns[pn]
                pn += 1 
            isN = not isN
        if (isN and (len(ns) - pn - 1) > 0) or (not isN and (len(cs)-ps-1) > 0):
            return ''
        else:
            while pn < len(ns):
                re += ns[pn]
                pn += 1 
            while ps < len(cs):
                re += cs[ps]
                ps += 1 
            return re


s = Solution()
m = s.reformat
cases = [
    ['1229857369'],
    ['covid2019'],
    ['ab123']
]

for case in cases:
    print(m(*case))