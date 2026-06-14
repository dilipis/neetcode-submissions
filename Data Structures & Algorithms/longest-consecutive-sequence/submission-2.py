class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_nums = []
        set_nums = ()

        if len(nums) in (0,1) :
            return len(nums)
        
        # Remove dupes
        set_nums = set(nums)
        # Sort
        sort_nums = sorted(set_nums)

        # print(f"{set_nums=}\n{sort_nums=}")

        # Set smallest seq = 0
        max_seq,ctr = 0,0
        # Iterate to find seq, Set seq to 1 if any found
        for i in range(len(sort_nums) - 1):
            if sort_nums[i+1] == sort_nums[i] + 1:
                ctr+= 1
                if ctr > max_seq :
                    max_seq = ctr
            else:    # Seq broken. Reset seq ctr
                ctr = 0

        return max_seq + 1
        