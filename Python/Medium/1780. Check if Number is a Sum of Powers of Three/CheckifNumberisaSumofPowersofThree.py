class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        powersofThree = []
        for i in range(n):
            if pow(3,i) <= n:
                powersofThree.append(pow(3,i))
            else:
                break
        
        for i in range(1,len(powersofThree)+1):
            if powersofThree[-i] <= n:
                n -= powersofThree[-i]
            
        if n == 0:
            return True
        else:
            return False

        
                
                







sol = Solution()
print(sol.checkPowersOfThree(91))