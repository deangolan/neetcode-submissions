class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        subs = []
        positions = {}
        for i, char in enumerate(s):
            if char in positions:
                positions[char][1] = i
            else:
                positions[char] = [i, i]
        partition_start = 0
        partition_end = 0
        # print(positions)
        for start, end in positions.values():
            # print(partition_end)
            if start > partition_end:
                subs.append(partition_end - partition_start + 1)
                partition_start = start
            partition_end = max(partition_end, end)
        subs.append(partition_end - partition_start + 1)

        return subs