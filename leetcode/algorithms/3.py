class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        d = {}
        l = 0
        r = 0
        re = 0
        n = len(s)
        while r < n:
            cur = s[r]
            if s[r] in d:
                nexl = d[cur] + 1
                for i in range(l, nexl):
                    del d[s[i]]
                l = nexl
                d[cur] = r
            else:
                d[cur] = r
                re = max(re, r - l + 1)
            r += 1
        return re

s = Solution()
print(s.lengthOfLongestSubstring('tmmzuxt'))