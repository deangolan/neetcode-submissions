class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i, n in enumerate(nums[0:len(nums)-2]):
            if n > 0:
                break

            if i > 0 and n == nums[i-1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            while l < r:
                ln = nums[l]
                rn = nums[r]
                if ln + rn < -n:
                    l += 1
                elif ln + rn > -n:
                    r -= 1
                else:
                    res.append([n, ln, rn])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res