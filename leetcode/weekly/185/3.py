from typing import List

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        nums = {
            'c': 0,
            'r': 0,
            'o': 0,
            'a': 0,
            'k': 0
        }
        for c in croakOfFrogs:
            if c not in nums:
                return -1
            nums[c] += 1
        num = nums['c']
        for k,v in nums.items():
            if v != num:
                return -1
        d = {
            'c': 0,
            'r': 1,
            'o': 2,
            'a': 3,
            'k': 4
        }
        ws = []
        wd = {
            0: set(),
            1:set(),
            2:set(),
            3:set(),
            4:set()
        }
        for c in croakOfFrogs:
            if c not in d:
                return -1
            cur = d[c]
            if cur == 0:
                curws = wd[cur]
                if len(curws) < 1:
                    ws.append(1)
                    index = len(ws) - 1
                    wd[1].add(index)
                else:
                    index = curws.pop()
                    ws[index] = 1
                    wd[1].add(index)
            else:
                curws = wd[cur]
                if len(curws) < 1:
                    return -1
                else:
                    index = curws.pop()
                    if cur == 4:
                        ws[index] = 0
                        wd[0].add(index)
                    else:
                        ws[index] += 1
                        wd[ws[index]].add(index)
        for w in ws:
            if w != 0:
                return -1
        return len(ws)



s = Solution()
m = s.minNumberOfFrogs
cases = [
    "croakcroak",
    'crcoakroak',
    'croakcrook',
    'croakcroa'
]

for case in cases:
    print(m(case))