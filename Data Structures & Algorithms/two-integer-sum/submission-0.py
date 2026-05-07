class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            j = seen.get(num, None)
            if j is not None:
                return [j, i]
            seen[target - num] = i
        return []