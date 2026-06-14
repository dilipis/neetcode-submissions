class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Remove non alphanumeric chars and make lowercase
        s = "".join([c.lower() for c in s if c.isalnum()])

        fctr = 0
        bctr = len(s) - 1
        isPal = True

        print(f"{s=}")

        print(f"{fctr=}\n{bctr=}")

        # Traverse from both sides. If correpding items are same, continue, else break
        while fctr <= bctr:
            print(f"{fctr=},{bctr=},{s[fctr]=},{s[bctr]=}")
            if s[fctr] != s[bctr]:
                isPal = False
                break
            fctr += 1
            bctr -= 1

        return isPal

        