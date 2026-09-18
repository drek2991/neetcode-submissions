class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        best = 1
        left = 0
        right = 1
        chars = set()
        chars.add(s[0])
        while right < len(s):
            if s[right] in chars:
                while s[left] != s[right]:
                    chars.remove(s[left])
                    left+=1
                left += 1
                right += 1
            else:
                chars.add(s[right])
                best = max(best, right-left+1)
                right += 1
        return best