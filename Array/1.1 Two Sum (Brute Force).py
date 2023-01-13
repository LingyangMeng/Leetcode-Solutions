class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            firstNum = nums[i]
            for j in range(i + 1, len(nums)):
                secondNum = nums[j]
                if firstNum + secondNum == target:
                    return [i, j]

        return []
