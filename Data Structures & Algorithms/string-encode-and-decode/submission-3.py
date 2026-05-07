class Solution:
    def encode(self, strs: List[str]) -> str:
        lens = []
        for s in strs:
            lens.append(str(len(s)))
        return ",".join(lens) + "#" + "".join(strs)
    
    def decode(self, s: str) -> List[str]:
        lens = []
        acc = []
        for i, char in enumerate(s):
            if char == ",":
                lens.append(int("".join(acc)))
                acc = []
            elif char == "#":
                lens.append(int("".join(acc))) if acc != [] else None
                start = i + 1
                break
            else: # char must be a digit
                acc.append(char)
            
        strs = []
        offset = 0
        for l in lens:
            strs.append(s[start+offset:start+l])
            start += l

        return strs
