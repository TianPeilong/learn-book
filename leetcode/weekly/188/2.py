from typing import List



s = Solution()
m = s.displayTable
cases = [
    [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
]

for case in cases:
    print(m(case))