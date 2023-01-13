class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        l, r = 0, 1

        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            else:
                l += 1
                r += 1
        
        return False
