class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        spec = {
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM"
        }
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        r = ""
        i = 0
        while num > 0:           
            while i < 13:
                if num <= 0:
                    break
                v = value[i]
                if num >= v:
                    r += symbol[i]
                    num -= v
                else:
                    i += 1
        return r

if __name__ == "__main__":
    num = 1994
    t = Solution()
    print(t.intToRoman(num))
    input()