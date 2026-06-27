class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use a dictionary to store counts
        charct_s = {}
        charct_t = {}

        # First check if they are of equal length
        if len(s) != len(t):
            return False

        # Create a dict for counting chars. Same loop since lenths are same
        for i,c in enumerate(s):
            charct_s[c] = charct_s.get(c, 0) + 1
            charct_t[t[i]] = charct_t.get(t[i], 0) + 1

        # Compare if the dictionaries match
        for k,v in charct_s.items():
            if not (k in charct_t and charct_t[k] == v):
                return False

        return True





        