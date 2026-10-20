class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        count = 0
        while i < len(word) and j < len(abbr):
            print(i, j)
            while count > 0:
                i += 1
                count -= 1
            if abbr[j].isdigit():
                val = int(abbr[j])
                if val == 0:
                    return False
                while abbr[j].isdigit():
                    count *= 10
                    count += val
                    j += 1
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        if i != len(word) and j != len(abbr):
            return False        
        return True
                

