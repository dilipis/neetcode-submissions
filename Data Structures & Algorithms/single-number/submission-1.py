class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # Any number XORed with iteself is 0 and cancels out.
        # Since there is only a single non duplicate, all other numbers cancel out and the 
        # non duplicate remains
        for n in nums:
            res = n ^ res

        return res

        