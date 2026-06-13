class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Dict to store output. Key -> number, value -> occurrence
        d_occ = defaultdict(int)

        # List to store the frequency. It is a 2D list with the no: of occurrences as the
        # key and a list of numbers with those reccurrences as the value
        freq = [[] for n in range(len(nums) + 1)]

        res = []    # Result list

        #Loop through list, and add to dict. Update ctr as well
        for n in nums:
            d_occ[n] += 1

        # Populate the result array
        for n,c in d_occ.items():
            freq[c].append(n)

        # Loop in reverse through and find top k items
        for i in range(len(freq)-1,0,-1):
            # Lopp through each element in the sublist
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res       



        


        