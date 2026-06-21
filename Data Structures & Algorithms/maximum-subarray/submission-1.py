class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sub = nums[0]

        for n in nums:
            # If cumulative sum till now is -ve, ignore sum and reset to 0
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += n   
            max_sub = max(max_sub, cur_sum)

        return max_sub
            


 

        