from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = [{} for i in range(501)]
        foods = set()
        for od in orders:
            tb = tables[int(od[1])]
            food = od[2]
            if food not in tb:
                tb[food] = 1
            else:
                tb[food] += 1
            foods.add(food)
        re = []
        foods = sorted(foods)
        n = len(foods)
        fm = {}
        for i,f in enumerate(foods):
            fm[f] = (i + 1)
        h = ['Table']
        h.extend(foods)
        re.append(h)
        i = 1
        while i < 501:
            if len(tables[i]) > 0:
                cur = ['0'] * (n + 1)
                cur[0] = str(i)
                for k,v in tables[i].items():
                    cur[fm[k]] = str(v)
                re.append(cur)
            i += 1
        return re


s = Solution()
m = s.displayTable
cases = [
    [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
]

for case in cases:
    print(m(case))