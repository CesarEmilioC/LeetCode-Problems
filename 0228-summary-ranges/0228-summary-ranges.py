class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #Especial cases
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return ["{}".format(nums[0])]
        #We sort the array
        nums.sort()
        #List to have the ranges
        list_ranges = []
        #Varibale for pivot and last of range
        pivot = nums[0]
        last_of_range = nums[0]
        #Cycle to check the ranges
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                last_of_range += 1
                #Case when the last number is not in a sequence
                if i == len(nums) - 1:
                    list_ranges.append("{}->{}".format(pivot, last_of_range))
            else:
                #Check if the range envolves more than one number
                if last_of_range - pivot > 0:
                    list_ranges.append("{}->{}".format(pivot, last_of_range))
                else:
                    list_ranges.append("{}".format(pivot))
                pivot = nums[i]
                last_of_range = nums[i]
                print(pivot)
                #Case when the last number is not in a sequence
                if i == len(nums) - 1:
                    list_ranges.append("{}".format(pivot))
        return list_ranges
        