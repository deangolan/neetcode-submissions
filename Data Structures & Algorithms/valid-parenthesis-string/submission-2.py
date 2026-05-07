class Solution:
    def checkValidString(self, s: str) -> bool:
        parens = []
        stars = []
        for i, char in enumerate(s):
            if char == '(':
                parens.append(i)
            if char == ')':
                if len(parens) != 0:
                    parens.pop()
                elif len(stars) != 0:
                    stars.pop()
                else:
                    return False
            if char == '*':
                stars.append(i)

        while len(parens) != 0 and len(stars) != 0:
            if parens[-1] > stars[-1]:
                return False
            parens.pop()
            stars.pop()

        return len(parens) == 0