class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_list = ["[", "(", "{"]
        for char in s:
            if char in open_list:
                stack.append(char)
            elif not stack:
                return False
            else:
                val = stack.pop()
                if val == "{" and char != "}":
                    return False
                elif val == "[" and char != "]":
                    return False
                elif val == "(" and char != ")":
                    return False
        if stack:
            return False

        return True
