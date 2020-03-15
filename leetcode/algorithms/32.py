class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        pr = {}
        cache = []
        last_pop = None
        for i, c in enumerate(s):
            if not cache:
                if last_pop is not None:
                    pr[last_pop] = i - last_pop
                cache.append((c,i))
                last_pop = None
            else:
                if c == cache[-1][0]:
                    if last_pop is not None:
                        pr[last_pop] = i - last_pop
                        last_pop = None                 
                    cache.append((c,i))
                else:
                    p = cache.pop()
                    last_pop = p[1]
        if last_pop is not None:
            pr[last_pop] = len(s) - last_pop
        ml = 0
        p = set()
        for i, l in pr.items():
            if i in p:
                continue
            cl = pr[i]
            next_index = i + pr[i]
            while next_index in pr:
                next_l = pr[next_index]
                cl += next_l
                p.add(next_index)
                next_index += next_l
            if cl > ml:
                ml = cl
            pr[i] = cl
        return ml
                        

p = ")("
t = Solution()
print(t.longestValidParentheses(p))
input()