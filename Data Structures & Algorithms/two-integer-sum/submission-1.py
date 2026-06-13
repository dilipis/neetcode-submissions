class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: num, value: index in array
        prevMap = {}

        for i,val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return[prevMap[diff],i]
            
            # Add number to dictionary
            prevMap[val] = i

        return

        