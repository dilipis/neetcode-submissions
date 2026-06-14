class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        
        # Remove non alphanumeric chars and make lowercase
        # s = "".join([c.lower() for c in s if c.isalnum()])
        s = re.sub(r'[^a-zA-Z0-9]','',s).lower()

        fctr = 0
        bctr = len(s) - 1
        isPal = True

        # Traverse from both sides. If correpding items are same, continue, else break
        while fctr <= bctr:
            if s[fctr] != s[bctr]:
                isPal = False
                break
            fctr += 1
            bctr -= 1

        return isPal

        