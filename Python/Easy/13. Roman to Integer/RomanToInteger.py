class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDic = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        nextTurn = False
        number = 0

        for x in range(len(s)):

            if nextTurn:
                nextTurn = False
                continue
            if x != len(s)-1:
                if s[x] == "I":
                    if s[x+1] == "X":
                        number += (romanDic[s[x+1]] - romanDic[s[x]])
                        nextTurn = True
                        continue
                    elif s[x+1] == "V":
                        number += (romanDic[s[x+1]] - romanDic[s[x]])
                        nextTurn = True
                        continue
                elif s[x] == "X":
                    if s[x+1] == "C":
                        number += (romanDic[s[x+1]] - romanDic[s[x]])
                        nextTurn = True
                        continue
                    elif s[x+1] == "L":
                        number += (romanDic[s[x+1]] - romanDic[s[x]])
                        nextTurn = True
                        continue
                elif s[x] == "C":
                    if s[x+1] == "D":
                        number += (romanDic[s[x+1]] - romanDic[s[x]])
                        nextTurn = True
                        continue
                    elif s[x+1] == "M":
                        number += (romanDic[s[x+1]] - romanDic[s[x]])
                        nextTurn = True
                        continue
            

            number += romanDic[s[x]]
        
        return number