from math import prod 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l=0
        res = []
        n=len(nums)

        for i in range(len(nums)):
            left = prod(nums[0:i])
            right = prod(nums[i+1:n])

            l = left*right
            res.append(l)

        return res    