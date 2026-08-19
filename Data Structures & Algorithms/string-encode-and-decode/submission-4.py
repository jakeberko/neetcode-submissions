from collections import deque
class Solution:
    str_amounts = deque()
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += string
            self.str_amounts.appendleft(len(string))
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        start_ptr = 0
        end_ptr = 0
        while self.str_amounts:
            str_len = self.str_amounts.pop()
            start_ptr = end_ptr
            end_ptr += str_len
            cur_str = s[start_ptr:end_ptr]
            res.append(cur_str)
        
        return res


