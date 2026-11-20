class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        
        # Case 1: 2 or more zeros -> everything becomes 0
        if zeros >= 2:
            return [0] * len(nums)
            
        # Multiply all non-zero numbers together
        total_prod = 1
        for x in nums:
            if x != 0:
                total_prod *= x
                
        # Case 2: Exactly 1 zero -> only the zero's position gets total_prod
        if zeros == 1:
            return [total_prod if x == 0 else 0 for x in nums]
            
        # Case 3: No zeros -> total product divided by current number
        return [total_prod // x for x in nums]