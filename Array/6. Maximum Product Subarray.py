class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = max(tmp, curMin * n, n)
            res = max(curMax, res)
        
        return res