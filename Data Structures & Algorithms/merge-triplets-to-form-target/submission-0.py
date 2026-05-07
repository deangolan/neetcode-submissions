class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        found = [False, False, False]
        for triplet in triplets:
            if triplet[0] == a and triplet[1] <= b and triplet[2] <= c:
                found[0] = True
            if triplet[0] <= a and triplet[1] == b and triplet[2] <= c:
                found[1] = True
            if triplet[0] <= a and triplet[1] <= b and triplet[2] == c:
                found[2] = True

        return all(found)
            
