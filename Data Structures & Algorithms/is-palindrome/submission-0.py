class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered=[w.lower() for w in s if w.isalnum()]
        return filtered==filtered[::-1]