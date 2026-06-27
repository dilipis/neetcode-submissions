class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tup_nums = set()
        for n in nums:
            if n in tup_nums:
                return True
            tup_nums.add(n)
        
        return False

