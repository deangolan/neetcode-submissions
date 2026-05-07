class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        longest = 1
        cur = 1

        i = 0
        j = 1
        expect = None
        while j < len(arr):
            k = arr[i]
            if k < arr[j]:
                if not expect or expect == "LT":
                    cur += 1
                else:
                    cur = 2
                expect = "GT"
            elif k > arr[j]:
                if not expect or expect == "GT":
                    cur += 1
                else:
                    cur = 2
                expect = "LT"
            else:
                expect = None
                cur = 1

            longest = max(longest, cur)
            i += 1
            j += 1

        return longest