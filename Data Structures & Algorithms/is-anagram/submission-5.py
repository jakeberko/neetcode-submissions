class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_tracker = {}
        count = 0
        if len(s) != len(t):
            return False

        for char in s:
            if char in string_tracker:
                string_tracker[char] += 1
            else:
                string_tracker[char] = 1

        for char in t:
            if char not in string_tracker:
                return False
            else:
                if string_tracker[char] == 0:
                    return False
                else:
                    string_tracker[char] -= 1
        
        if count != 0:
            return False
        return True