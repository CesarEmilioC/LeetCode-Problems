'''
Cesar Emilio Castaño Marin
Solution: Two Sum
Github Username: CesarEmilioC
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Loop to go through nums
        for i in nums:
            #We create a difference variable
            d = target-i
            try:
                #We try to search the difference in nums
                return [nums.index(i),nums.index(d,nums.index(i)+1)]
                break
            except:
                pass
        