class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        preMap = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            preMap[course].append(pre)

        cycle = set()
        taken = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in taken:
                return True
            
            cycle.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            taken.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res