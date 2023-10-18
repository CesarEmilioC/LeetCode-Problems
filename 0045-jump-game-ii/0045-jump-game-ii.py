'''
Cesar Emilio Castaño Marin
Solution: Jump Game II
Github Username: CesarEmilioC
'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #We try to think in reverse, because we must get to the last number in the list
        nums.reverse()
        numero_de_saltos = 0
        #We are going to modify the list on every jump
        while len(nums) != 1:
            #We jump to the last possible number in the reversed list nums from which we can jump to the new first position (Which correspond to the last number of the normal actual num list)
            for i in range(len(nums)-1,0,-1):
                if i <= nums[i]:
                    numero_de_saltos += 1
                    nums = nums[i:]
                    break
        return numero_de_saltos

       