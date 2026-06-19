class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            mid = (rp+lp) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                # Left half
                rp = mid - 1
            else:
                # Right half
                lp = mid + 1

        return -1
