class Solution:
    def isValid(self, s: str) -> bool:

        #Stack to be used so that order can be checked
        stack = []

        # Create dictionary for mapping closing brackets
        dicClose = {")" : "(", "]" : "[", "}" : "{"}

        # Loop through string. Add Opening brackets to stack. 
        # If closing bracket, pop from stack if last opening bracket matches

        for c in s:
            # If opening bracket, add to stack
            if c not in dicClose:
                stack.append(c)
            elif stack:
                # If closing, ensure that the top element in stack is corresp. opening bracket 
                if dicClose[c] == stack[-1]:
                    stack.pop()
                else:
                    #clsoing brackets dot match. Exit
                    return False
            else:
                # Closing bracket but stack empty. 
                return False

        # If code reaches here, check if stack empty. If so everything is synced
        return True if len(stack) == 0 else False



        