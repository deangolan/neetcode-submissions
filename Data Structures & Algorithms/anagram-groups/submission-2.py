class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            freqs = [0] * 26
            for ch in s:
                freqs[ord('a') - ord(ch)] += 1
            groups[tuple(freqs)].append(s)
        return list(groups.values())