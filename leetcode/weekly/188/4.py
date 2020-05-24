from typing import List

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        CONSTN = 10**9 + 7
        acs = [[[0]*2 for j in range(len(pizza[0])+1)] for i in range(len(pizza)+1)]
        counts = [[0 for j in range(len(pizza[0])+1)] for i in range(len(pizza)+1)]
        for ir,r in enumerate(pizza):
            for jc,cur in enumerate(r):
                if cur == 'A':
                    acs[ir+1][jc+1][0] = acs[ir+1][jc][0] + 1
                    acs[ir+1][jc+1][1] = acs[ir][jc+1][1] + 1
                else:
                    acs[ir+1][jc+1][0] = acs[ir+1][jc][0]
                    acs[ir+1][jc+1][1] = acs[ir][jc+1][1]
        cut = 1
        rnum = len(counts) - 1
        cnum = len(counts[0]) - 1
        counts[0][0] = 1
        while cut < k:
            cut += 1
            newcounts = [[0 for j in range(len(pizza[0])+1)] for i in range(len(pizza)+1)]
            for i in range(0,len(counts)):
                for j in range(0, len(counts[i])):
                    if i == rnum and j == cnum:
                        continue
                    curCount = counts[i][j]
                    if curCount > 0:
                        if i != rnum:
                            for r in range(i+1, rnum+1):
                                if acs[r][cnum][0] - acs[r][j][0] > 0:
                                    for nr in range(r, rnum+1):
                                        newcounts[nr][j] = (newcounts[nr][j] + curCount) % CONSTN
                                    break
                        if j != cnum:
                            for c in range(j+1, cnum+1):
                                if acs[rnum][c][1] - acs[i][c][1] > 0:
                                    for nr in range(c, cnum+1):
                                        newcounts[i][nr] = (newcounts[i][nr] + curCount) % CONSTN
                                    break
            counts = newcounts
        su = 0
        for i in range(0,len(counts)):
            for j in range(0, len(counts[i])):
                if i == rnum and j == cnum:
                    continue
                curCount = counts[i][j]
                if curCount > 0:
                    if i != rnum:
                        for r in range(i+1, rnum+1):
                            if acs[r][cnum][0] - acs[r][j][0] > 0:
                                su = (su + curCount) % CONSTN
                                break
                    else:
                        if j != cnum:
                            for c in range(j+1, cnum+1):
                                if acs[rnum][c][1] - acs[i][c][1] > 0:
                                    su = (su + curCount) % CONSTN
                                    break
        return su % CONSTN



        



s = Solution()
m = s.ways
cases = [
    [["A..","A..","..."],1]
]

for case in cases:
    print(m(*case))