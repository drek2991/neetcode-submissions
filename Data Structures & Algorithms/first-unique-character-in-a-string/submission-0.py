class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = -1
        for char in d:
            if d[char] > -1:
                return d[char]
        return -1

            
