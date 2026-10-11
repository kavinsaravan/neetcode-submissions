class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping:
            # Check if the stack matches the expected opening bracket
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack