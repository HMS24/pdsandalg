"""https://leetcode.com/problems/course-schedule/
"""

# Approach 1 dfs
# Time Limit Exceeded
class Solution_1:
    def canFinish(self, numCourses, prerequisites):
        deps_dict = {}
        for take, need in prerequisites:
            if need in deps_dict:
                deps_dict[need].append(take)
            else:
                deps_dict[need] = [take]
        
        path = set()
        for target in range(numCourses):
            path.clear()
            if not self.dfs(target, deps_dict, path):
                return False
        return True

    def dfs(self, target, deps_dict, path):
        if target in path:
            return False
        if target not in deps_dict:
            return True
            
        for course in deps_dict[target]:
            path.add(course)
            if not self.dfs(course, deps_dict, path):
                return False
            path.remove(course)
        return True

# Approach 2 dfs - improved
class Solution_2:
    def canFinish(self, numCourses, prerequisites):
        checked = set()
        deps_dict = {}
        for target, need in prerequisites:
            if target in deps_dict:
                deps_dict[target].append(need)
            else:
                deps_dict[target] = [need]
                
        checking = set()
        for target in range(numCourses):
            checking.clear()
            if not self.dfs(target, deps_dict, checking, checked):
                return False
        return True

    def dfs(self, target, deps_dict, checking, checked):
        if target in checked:
            return True
        if target not in deps_dict:
            checked.add(target)
            return True
        if target in checking:
            return False
            
        checking.add(target)
        for dep_course in deps_dict[target]:
            if not self.dfs(dep_course, deps_dict, checking, checked):
                return False
        checked.add(target)
        return True