class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        max_count = 0
        char_map = {}
        for i, char in enumerate(s):
            if char in char_map:
                if max_count < count:
                    max_count = count
                idx = char_map[char]
                if count >= i-idx:
                    count = i - idx
                else: 
                    count += 1
                char_map[char] = i
            else:
                char_map[char] = i
                count += 1
        if max_count < count:
            max_count = count
        return max_count



        