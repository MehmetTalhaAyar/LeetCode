class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
       
        if nums.count(val) > 0:
            counter = nums.count(val)
            for y in range(0,counter):
                nums.remove(val)
        
        return len(nums)