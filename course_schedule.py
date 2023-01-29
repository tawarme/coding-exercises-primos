class Solution(object):
    def go(self, course, courses, explored):
        #print("Exploring", course)
        #print("explored",explored)
        #print("path",explore_path)

        if explored.get(course):
            return False

        if courses.get(course) is None:
            return True

        explored[course] = True

        for pre in courses[course]:
            if not self.go(pre, courses, explored):
                return False
        
        courses[course] = None
        del explored[course]
        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        courses = {}
        for course, pre in  prerequisites:
            if courses.get(pre):
                courses[pre].append(course)
            else:
                courses[pre] = [course]

      
        explored = {}
        for course in courses:
            if not self.go(course, courses, explored):
                return False
        
        return True
