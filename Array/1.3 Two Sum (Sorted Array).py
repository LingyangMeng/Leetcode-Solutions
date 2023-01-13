class Solution(object):
    def twoSum(self, nums, target):
        nums.sort()
        l, r = 0, len(nums) - 1
        
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                return [nums[l], nums[r]]
                
        return
