class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        
        result = []

        temp = 0
        while temp < len(s):  
            result.append(s[temp:temp+k])
            temp = temp+k

        if len(result[-1]) != k:
            result[-1] += fill * (k-len(result[-1]))
        

        return result