class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        counter = len(needle)
        x = 0
        y = counter
        while True:
            if len(haystack) < y:
                y = None
            if haystack[x:y] == needle:
                return x
            
            if y == None:
                return -1

            x += 1
            y += 1