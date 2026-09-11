class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char
        a = new.lower()
        b = a[::-1]
        return a==b