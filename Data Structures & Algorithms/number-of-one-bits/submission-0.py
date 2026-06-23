class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0
        # For a binary number, mod 2 always gives 1 if last bit is 1. Else 0
        while n:
            res = res + (n % 2)
            # Fro the next run, shift the bits to the right so that each bit eventually moves to the 
            # rightmost position
            n = n >> 1

        return res
        