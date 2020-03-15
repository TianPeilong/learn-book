class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        t_dic = {}
        for w in words:
            if w in t_dic:
                t_dic[w] += 1
            else:
                t_dic[w] = 1
        result = []
        w_len = len(words[0])
        t_len = w_len * len(words)
        for i in range(len(s) - t_len + 1):
            look = t_dic.copy()
            j = i
            while len(look) > 0:
                sub = s[j: j + w_len]
                if sub in look:
                    v = look[sub]
                    v -= 1
                    if v == 0:
                        del look[sub]
                    else:
                        look[sub] = v
                    j += w_len
                else:
                    break
            if len(look) <= 0:
                result.append(i)
        return result

    def composeStrs(self, words):   
        if len(words) == 1:
            return set(words)
        else:
            s = set()
            for w in words:
                part_ws = list(words)
                part_ws.remove(w)
                part_s = self.composeStrs(part_ws)
                for p in part_s:
                    s.add(w + p)
            return s


if __name__ == "__main__":
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    t = Solution()
    print(t.findSubstring(s, words))
    input()