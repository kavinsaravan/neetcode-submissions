class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        leftStack = []
        rightStack = []

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                leftStack.append(s[left].lower())
                rightStack.append(s[right].lower())
                left += 1
                right -= 1
            elif (s[left].isalnum() == False):
                left += 1
            elif (s[right].isalnum() == False):
                right -= 1

        return leftStack == rightStack


        