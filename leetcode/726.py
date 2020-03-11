class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        cache = []
        dic = {}
        i = 0
        while i < len(formula):
            cur = formula[i]
            if cur == '(':
                cache.append(dic)
                dic = {}
                i += 1
            elif cur == ')':
                count_str = ''
                i += 1
                while i < len(formula):
                    if '0' <= formula[i] <= '9':
                        count_str += formula[i]
                    else:
                        break
                    i += 1
                count = 1 if count_str == '' else int(count_str)
                p_dic = cache.pop()
                for k,v in dic.items():
                    if k in p_dic:
                        p_dic[k] += v * count
                    else:
                        p_dic[k] = v * count
                dic = p_dic
            elif cur >= 'A' and cur <= 'Z':
                name = cur
                i += 1
                while i < len(formula):
                    if 'a' <= formula[i] <= 'z':
                        name += formula[i]
                    else:
                        break
                    i += 1
                count_str = ''
                while i < len(formula):
                    if '0' <= formula[i] <= '9':
                        count_str += formula[i]
                    else:
                        break
                    i += 1
                count = 1 if count_str == '' else int(count_str)
                if name in dic:
                    dic[name] += count
                else:
                    dic[name] = count
        result = ''
        for k, v in sorted(dic.iteritems(), key=lambda d:d[0], reverse = False):
            result += k
            if v > 1:
                result += str(v)
        return result

formula = 'K4(ON(SO3)2)2'
t = Solution()
print(t.countOfAtoms(formula))