class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = { course: [] for course in range(numCourses) }
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
            return True
            
        return all(validate(course) for course in range(numCourses)) 