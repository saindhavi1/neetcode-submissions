class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letters = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char not in letters:
                letters[char] = 0
            letters[char] += 1
            

        for char in t:
            if char in letters:
                letters[char] -= 1

        for key in letters:
            if letters[key] != 0:
                return False

        return True