from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        return self.minL(words, -1)
    
    def minL(self, words, pos):
        if not words:
            return 0
        if pos < -7:
            return 8
        R = 58
        arr = [[] for i in range(58)]
        l = abs(pos)
        emptys = []
        for w in words:
            if len(w) < l:
                emptys.append(w)
            else:
                arr[ord(w[pos])-65].append(w)
        if len(emptys) == len(words):
            return -pos
        pos -= 1
        s = 0
        for ws in arr:
            if ws:
                s += self.minL(ws, pos)
        return s

s = Solution()
words = ["mokgggq","pjdislx","bfrbsfs","hgwqzz","bnwxc"]
print(s.minimumLengthEncoding(words))