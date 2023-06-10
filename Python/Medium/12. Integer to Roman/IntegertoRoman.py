class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanDic = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M"
        }
        

        romanNumber = ""
        count = 0
        values = [1000,500,100,50,10,5,1]

        for x in range(len(values)):
            if num // values[x] >= 1 :
                count = num // values[x]
                romanNumber += romanDic[values[x]] * count
                num -= (num//values[x]) * values[x]

            if x % 2 == 0 and x != (len(values) - 1):
                if num // (values[x] - values[x+2]) == 1:
                    romanNumber += (romanDic[values[x+2]] + romanDic[values[x]])
                    num -= values[x] - values[x+2]
            elif x % 2 == 1:
                if num // (values[x] - values[x+1]) == 1:
                    romanNumber += (romanDic[values[x+1]] + romanDic[values[x]])
                    num -= values[x] - values[x+1]

        
        return romanNumber



    



sol = Solution()

print(sol.intToRoman(995))