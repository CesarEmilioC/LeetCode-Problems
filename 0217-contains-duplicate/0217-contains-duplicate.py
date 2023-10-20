'''
Cesar Emilio Castaño Marin
Solution: Contains Duplicate
Github Username: CesarEmilioC
Technique: Sort list and check if there are two equal adjacent elements
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        #If there were not two equal numbers, return False
        return False
        