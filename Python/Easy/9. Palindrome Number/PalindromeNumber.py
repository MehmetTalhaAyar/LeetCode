class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        myList = []
        while x >= 1:
            number = x % 10
            x = int(x / 10)
            myList.append(number)
        
        for x in range(len(myList)):
            if myList[x] != myList[-x-1]:
                return False
        
        return True
