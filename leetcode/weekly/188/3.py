from typing import List





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