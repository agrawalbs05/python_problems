# Check valid Paranthesis
# Tags: N20, Blind75, stack, Easy

def isValid(s):
    stack = []
    # Hash map for keeping track of mappings.clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")" :"(","}" : "{", "]" : "["}
        
    for i in s:
        if i in mapping: # That means it's closing parentheses
            if stack and stack[-1] == mapping[i]: # Check stack empty and last element is opening parentheses
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
                
    return True if not stack else False

# Time complexity :O(n)
# Space copmexity :O(n)

s = "()[]{}"
isValid(s)
