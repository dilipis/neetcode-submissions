class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i_out = [1] * len(nums)
        i_pref = [1] * len(nums)
        i_post = [1] * len(nums)
        prod = 1

        # Create prefix list
        for i in range(len(nums)):
            if i == 0:
                prod = 1
            else:
                prod *= nums[i-1]
            i_pref[i] = prod

        # Create postfix array
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums) - 1:
                prod = 1
            else:
                prod *= nums[i+1]
            i_post[i] = prod

        print(f"{i_pref=}\n{i_post=}")

        # Handle edge cases
        # Multiply
        for i in range(len(nums)):
            i_out[i] = i_pref[i] * i_post[i]

        return i_out