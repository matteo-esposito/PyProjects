class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        vals = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if ((nums[i] + nums[j] == target) and (i != j) and (i < j)):
                    vals = [i, j]
        
        return vals