class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = {}, {}
        # If diff length, def not anagaram
        if len(s) != len(t):
            return False
        # Get chars and count in dictionary
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i],0) + 1
            dict_t[t[i]] = dict_t.get(t[i],0) + 1
        # Compare each char count among arrays
        for k in dict_s:
            if dict_s[k] != dict_t.get(k,0):
                return False
        return True




        