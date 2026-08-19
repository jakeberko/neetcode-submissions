from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_tracker = defaultdict(int)
        if len(s) != len(t):
            return False

        for char in s: 
            string_tracker[char] += 1

        for char in t:
            if char not in string_tracker:
                return False
            else:
                if string_tracker[char] == 0:
                    return False
                else:
                    string_tracker[char] -= 1
        
        return True