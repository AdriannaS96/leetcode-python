class Solution:
    def firstUniqChar(self, s: str) -> int:


        letters = {}

        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        
        for index, char in enumerate(s):
            if letters[char] == 1:
                return index
        return -1


        
