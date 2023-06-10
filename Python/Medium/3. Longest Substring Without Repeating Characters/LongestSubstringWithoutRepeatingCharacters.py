class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longestSubstring = ""
        word = ""

        for i in range(len(s)):

            if longestSubstring == "":
                longestSubstring += s[i]
            else :
                if s[i] not in longestSubstring:
                    longestSubstring += s[i]
                else:
                    if len(longestSubstring) >= len(word):
                        word = longestSubstring
                       
                    for x in range(len(longestSubstring)):
                        if longestSubstring[x] == s[i]:
                            longestSubstring = longestSubstring[x+1:]
                            break

                    longestSubstring += s[i]


        
        if len(word) > len(longestSubstring):
            return len(word)
        else:
            return len(longestSubstring)