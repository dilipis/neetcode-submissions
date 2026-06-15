class Solution:
    def isValid(self, s: str) -> bool:

        #Stack to be used so that order can be checked
        stack = []

        # Create dictionary for mapping closing brackets
        dicClose = {")" : "(", "]" : "[", "}" : "{"}

        # Loop through string. Add Opening brackets to stack. 
        # If closing bracket, pop from stack if last opening bracket matches

        for c in s:
            print(f"{c=}, {stack=}")
            # If opening bracket, add to stack
            if c not in dicClose:
                stack.append(c)
                print(f"Opening bracket. {c=}, {stack=}")
            elif stack:
                # If closing, ensure that the top element in stack is corresp. opening bracket 
                if dicClose[c] == stack[-1]:
                    stack.pop()
                    print(f"Closing bracket. Pop. {c=}, {stack=}")
                else:
                    #clsoing brackets dot match. Exit
                    print(f"Closing bracket dont match. Exit. {c=}, {stack=}")
                    return False
            else:
                # Closing bracket but stack empty. 
                print(f"Closing bracket but stack empty. Exit. {c=}, {stack=}")
                return False

        # If code reaches here, check if stack empty. If so everything is synced
        return True if len(stack) == 0 else False



        