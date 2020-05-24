from typing import List




s = Solution()
m = s.reformat
cases = [
    ['1229857369'],
    ['covid2019'],
    ['ab123']
]

for case in cases:
    print(m(*case))