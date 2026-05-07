class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        for char in s1:
            target[char] = target.get(char, 0) + 1
        
        l = 0
        window = {}
        
        for r, char in enumerate(s2):
            window[char] = window.get(char, 0) + 1

            while target.get(char, 0) < window[char] and l < r:
                window[s2[l]] -= 1
                l += 1

            if all(count == window.get(char, 0) for char, count in target.items()):
                return True

        return False
