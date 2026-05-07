class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ')':
                if stack == []:
                    return False
                ch = stack.pop()
                if ch != '(':
                    return False
            elif c == ']':
                if stack == []:
                    return False
                ch = stack.pop()
                if ch != '[':
                    return False
            elif c == '}':
                if stack == []:
                    return False
                ch = stack.pop()
                if ch != '{':
                    return False
            else:
                stack.append(c)

        return stack == []