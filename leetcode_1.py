class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sIndex = 0
        eIndex = 0
            
        for n in range(0, len(nums)):
            eNum    = target - nums[n]
            if eNum in nums:
                for y in range(0,len(nums)):
                    if eNum == nums[y] and y > n:
                        sIndex = n
                        eIndex = y
                        
                    
        return [sIndex, eIndex]  
