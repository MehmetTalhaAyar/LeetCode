class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        counter = 0

        for i in words:
            for x in allowed:
                i = i.replace(x, "")

            
            if len(i) == 0:
                counter +=1


        return counter
