class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in words:
                words[sorted_word] = []
            words[sorted_word].append(word)
        ans = []
        for keys in words:
            ans.append(words[keys])
        return ans