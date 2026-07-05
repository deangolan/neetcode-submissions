class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = [] 

        prereqs = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        valid = set()
        path = set()
        def validate(course):
            if course in valid:
                return True
            
            if course in path:
                return False

            path.add(course)

            for prereq in prereqs[course]:
                if not validate(prereq):
                    return False

            path.remove(course)
            valid.add(course)
            order.append(course)
            return True

        for course in range(numCourses):
            if not validate(course):
                return []

        return order