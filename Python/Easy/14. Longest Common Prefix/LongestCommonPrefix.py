class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        counter = 0
        word = ""

        for x in range(len(strs[0])):
            for y in range(len(strs)):
                word = strs[0][x]
                if len(strs[y]) == x:
                    return strs[0][:counter]
                elif word != strs[y][x]:
                    return strs[0][:counter]
            
            counter +=1
        
        return strs[0][:counter]