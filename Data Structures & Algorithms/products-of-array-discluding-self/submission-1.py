class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i_out = [1] * len(nums)
        i_pref = [1] * len(nums)
        i_post = [1] * len(nums)
        prod = 1

        # Create prefix list
        for i in range(len(nums)):
            i_pref[i] = prod
            prod *= nums[i]

        # Create postfix array
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            i_post[i] = prod
            prod *= nums[i]

        # Handle edge cases
        # Multiply
        for i in range(len(nums)):
            i_out[i] = i_pref[i] * i_post[i]

        return i_out