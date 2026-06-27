class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Have a dictionary to store seen numbers
        seen = {}

        # Loop through the list. If element in seen list, return indices.
        # Else add to list
        for i,n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return([seen[diff],i])
            else:
                # Store number as key and index as value
                seen[n] = i

        
