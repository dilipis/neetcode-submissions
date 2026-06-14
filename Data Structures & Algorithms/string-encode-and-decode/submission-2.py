class Solution:

    def encode(self, strs: List[str]) -> str:
        # Concat all the strings into a single string using the format
        # <string length>#<string>
        enc = ''
        for s in strs:
            enc += str(len(s)) + "#" + s
        
        return enc

    def decode(self, s: str) -> List[str]:
        # Decode the single string using the known format
        
        dec, i = [], 0

        # Loop through string and find delimiter
        while i < len(s):
            # Pointer for finding delimiter
            j = i

            # Substring till delimiter = lenth of substring
            while s[j] != "#":
                j += 1
            s_len = int(s[i:j])
            # Substring from delimiter +1 to length of ss = word
            dec.append(s[j+1 : j + 1 + s_len])
            # Move string pointer to end of word + 1
            i = j + 1 + s_len

        return dec



