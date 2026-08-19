class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        s_t = s.lower()
        size = len(s_t)
        l = 0
        r = size - 1
        while l < r:
            if not s_t[l].isalnum():
                l = l+1
            elif not s_t[r].isalnum():
                r = r-1
            elif s_t[l] != s_t[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
