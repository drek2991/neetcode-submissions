class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):

            if abbr[j].isdigit():

                # leading zero check
                if int(abbr[j]) == 0:
                    return False

                # build full number
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num += num * 10 + int(abbr[j])
                    j += 1

                # move i forward by that number
                i += num

            else:
                # compare word[i] and abbr[j]
                # move both pointers
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)
                

