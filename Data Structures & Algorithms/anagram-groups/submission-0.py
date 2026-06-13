class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dictionary to hold output. Th key would be a list of 26, 
        # each representing the character count in a word
        res = defaultdict(list)

        for s in strs:
            # List for character count of each word. Initialized for all 26 alphabet to 0
            char_ctr = [0] * 26

            # Loop through each char in the word and update the char ctr. 
            # To map alphabet to 0 to 25, use ascii
            for c in s:
                char_ctr[ord(c) - ord("a")] += 1

            # Append list of words with exact same character count combo
            res[tuple(char_ctr)].append(s)

        return list(res.values())

        