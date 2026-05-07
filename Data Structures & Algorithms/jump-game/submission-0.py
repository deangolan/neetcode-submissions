class Solution:
    def canJump(self, nums: List[int]) -> bool:
        options = []
        i = 0
        while i < len(nums) - 1:
            n = nums[i]

            options = nums[i+1:i+n+1]
            if options == []:
                return False

            best_opt = [0, 0]
            for j, m in enumerate(options):
                score = j + m
                if score >= best_opt[1]:
                    best_opt = [j+1, score] 
            
            i += best_opt[0]
        
        return True