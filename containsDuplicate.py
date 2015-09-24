class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return False
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        