class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for x in nums:
            if nums.count(x) > 1:
                counter = nums.count(x)
                for y in range(0,counter-1):
                    nums.remove(x)

        return len(nums)