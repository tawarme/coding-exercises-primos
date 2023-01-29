class Solution:
    def go(self, course, courses, explored, ordering, added):
        if explored.get(course):
            return False

        if courses.get(course) is None:
            if not added.get(course):
                added[course] = True
                ordering.append(course)
            return True

        explored[course] = True

        for pre in courses[course]:
            if not self.go(pre, courses, explored, ordering, added):
                return False

        del explored[course]
        courses[course] = None

        if not added.get(course):
            added[course] = True
            ordering.append(course)

        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {}
        for course, pre in prerequisites:
            if courses.get(course):
                courses[course].append(pre)
            else:
                courses[course] = [pre]

        #print(courses)

        ordering = []
        
        explored = {}
        added = {}
        
        #for course in courses:
        for course in range(numCourses):
            if not self.go(course, courses, explored, ordering, added):
                #print("Dead exploring course", course)
                return []

        return ordering
