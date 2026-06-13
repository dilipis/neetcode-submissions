class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        idx = []
        for i,num in enumerate(nums):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    idx.append(i)
                    idx.append(j)
                    break

        return sorted(idx)
        